people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}, {'name': 'john', 'age': 7}]

def age(name):
    for i in people:
        if i["name"] == name:
            print(i["age"])
        else:
            print("명단에 없습니다.")

age("john")