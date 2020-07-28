import random
r = random.randint(1,100)
while True:
    answer = input('請輸入數字: ')
    answer = int(answer)
    if answer > r :
        print('不對,再小一點!')
    elif answer < r:
        print('不對,再大一點!')
    elif answer == r:
        print('恭喜你終於猜對了!!')
        break
    