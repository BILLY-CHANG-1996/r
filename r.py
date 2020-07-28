import random
start = input('請決定隨機數字開始值')
end = input('請決定隨機數字結束值')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count += 1 # count = count + 1
    answer = input('請輸入數字: ')
    answer = int(answer)
    if answer > r :
        print('不對,再小一點!')
    elif answer < r:
        print('不對,再大一點!')
    elif answer == r:
        print('恭喜你終於猜對了!!')
        print('這是你猜的', count, '次')
        break
    print('這是你猜的', count, '次')