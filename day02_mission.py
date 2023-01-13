#Chapter 4 Excercise

#4.1
import random
secret_number=random.randint(1,10)
guess_number=int(input("추측하는 숫자를 입력하세요(1~10):"))

if secret_number==guess_number:
    print("Just Right!")
elif secret_number>guess_number:
    print("Too high")
elif secret_number<guess_number:
    print("Too low")
