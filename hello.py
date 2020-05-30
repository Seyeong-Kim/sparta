fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def fruits_count(name):
    count = 0
    for i in fruits:
        if i == name:
            count += 1
    return count
subak_count = fruits_count("수박")
print(subak_count)