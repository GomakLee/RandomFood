import time
import random

lunch = ["짜장면","마라탕","치킨","떡볶이","김치찌개","보쌈"]

#점심 추가하기
while True:
    print(lunch)
    food = input("음식을 추가하세요 (멈추고 싶으면 q를 입력 하세요.) : ")
    if food == "q":
        break
    else:       
        lunch.append(food)
print(lunch)

#점심 삭제하기 
set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("음식을 삭제하세요 (멈추고 싶으면 q를 입력 하세요.) : ")
    if item == "q":
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch)

print("5초 후 랜덤으로 음식이 선택됩니다.")
for k in range(5,0,-1):
    print(k)
    time.sleep(1)
set_lunch = list(set_lunch)
print(random.choice(set_lunch))
