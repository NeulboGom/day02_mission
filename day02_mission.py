#Chapter 4 Excercise

#4.1
import random
secret_number=random.randint(1,10)
count=0

while True:
    guess_number = int(input("추측하는 숫자를 입력하세요(1~10):"))
    count+=1
    if secret_number == guess_number:
        print("Just Right!")
        break
    elif secret_number > guess_number:
        print("Too low")
    elif secret_number < guess_number:
        print("Too high")
print(f"{count}번만에 맞추셨습니다")