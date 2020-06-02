from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/TOrders', methods=['POST'])
def write_review():

    TOrderNameReceive = request.form["TOrderNameGive"]
    TOrderCountReceive = request.form["TOrderCountGive"]
    TOrderAddressReceive = request.form["TOrderAddressGive"]
    TOrderNumberReceive = request.form["TOrderNumberGive"]

    TOrder = {
        "TOrderName" : TOrderNameReceive,
        "TOrderCount" : TOrderCountReceive,
        "TOrderAddress" : TOrderAddressReceive,
        "TOrderNumber" : TOrderNumberReceive
    }

    db.TOrder.insert_one(TOrder)

    return jsonify({'result':'success', 'TOrders': '주문 완료'})


@app.route('/TOrders', methods=['GET'])
def read_reviews():

    TOrder = list(db.TOrder.find({},{'_id':0}))

    return jsonify({'result':'success', 'TOrders': TOrder})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)