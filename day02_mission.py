#Chapter 4 Excercise

#4.1
import random
a=1
b=10
secret_number=random.randint(a,b)
count=0

while True:
    guess_number = int(input("추측하는 숫자를 입력하세요(1~10):"))
    count+=1
    if secret_number == guess_number:
        print("Just Right!")
        break
    if guess_number not in range(a,b):
        print("범위 밖의 숫자입니다. 다시 입력하세요.")
    if secret_number > guess_number:
        b=guess_number-1
        print("Too low")
    elif secret_number < guess_number:
        a=guess_number+1
        print("Too high")
print(f"{count}번만에 맞추셨습니다. 프로그램을 종료합니다.")