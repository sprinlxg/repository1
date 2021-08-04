import random
num = random.randint(1,5)
count = 0
pwd = 123
blood = 2000
c = "yes"
a = int(input("请输入密码："))
if pwd == a :
    while True :
        count = count + 1
        chose = input("请您输入猜测的数字：")
        chose = int(chose)
        if blood > 0 :
            if chose > num :
                print("大了，大了")
                blood = blood - 500
            elif chose < num :
                print("小了，小了")
                blood = blood - 500
            else:
                print("猜中了获得奖励1000，本次神秘数字是：",num,"您猜了：",count,"次",blood)
                blood = blood + 1000
                print("您中了大奖是否继续游戏》》》》》，")
                b = input("继续游戏输入：")
                if c == b :
                    chose = input("请您输入猜测的数字：")
                    chose = int(chose)
                    if blood > 0:
                        if chose > num:
                            print("大了，大了")
                            blood = blood - 500
                        elif chose < num:
                            print("小了，小了")
                            blood = blood - 500
                        else:
                            print("猜中了获得奖励1000，本次神秘数字是：", num, "您猜了：", count, "次",blood)
                            blood = blood + 1000
                            break



                else:
                    break


        else:
            print("金币不足")
            break

else:
    print("密码错误！！！！！！！")

