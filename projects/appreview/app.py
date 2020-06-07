import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

#driver = webdriver.Chrome("./chromedriver")
#res = driver.get("https://play.google.com/store/apps/details?id=com.ncsoft.lineage2m19&showAllReviews=true")
#time.sleep(10)
#b1 = driver.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div:nth-child(1) > div.ry3kXd.Ulgu9 > div.MocG8c.UFSXYb.LMgvRb.KKjvXb > span')
#b1.click()
#time.sleep(2)
#b2 = driver.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div.OA0qNb.ncFHed > div:nth-child(1)')
#b2.click()
#time.sleep(10)
##driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
##time.sleep(10)
#
#reviews = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > div > div > div > div.d15Mdf.bAhLNe > div.UD7Dzf > span:nth-child(1)")
#clicks = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > div > div > div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.YCMBp.GVFJbb > div > div.XlMhZe > div.jUL89d.y92BAb")
#dates = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > div > div > div > div.d15Mdf.bAhLNe > div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.p2TkOb")
#
#
#for date,click,review in zip(dates,clicks,reviews):
#    if click.text == '':
#        db.appreviews.insert_one({"date" : date.text, "click" : 0, "review" : review.text})
#    else:
#        db.appreviews.insert_one({"date" : date.text, "click" : int(click.text), "review" : review.text})
#
#driver.close()

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/appreviews/list', methods=['GET'])
def appreviews():
    appreviews = list(db.appreviews.find({},{'_id':False}))
    return jsonify({'result': 'success','msg': appreviews})


#@app.route('/api/like', methods=['POST'])
#def star_like():
#    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#    name_receive = request.form["name_give"]
#    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
#    star = db.mystar.find_one({"name" : name_receive})
#    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
#    new_like = star["like"] + 1
#    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
#    db.mystar.update_one({"name" : name_receive}, {"$set" : {"like" : new_like}})
#    # 참고: '$set' 활용하기!
#    # 5. 성공하면 success 메시지를 반환합니다.
#    return jsonify({'result': 'success','msg':'like 연결되었습니다!'})
#
#
#@app.route('/api/delete', methods=['POST'])
#def star_delete():
#    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#    name_receive = request.form["name_give"]
#    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
#    db.mystar.delete_one({"name" : name_receive})
#    # 3. 성공하면 success 메시지를 반환합니다.
#    return jsonify({'result': 'success','msg':'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)