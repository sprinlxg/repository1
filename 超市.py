import  random
# 超市菜单
shop = [
    ["lenovo PC",5600],
    ["HUA WEI WATCH",1200],
    ["Mac pro",12000],
    ["洗衣机",3000],
    ["机械革命",5000],
    ["卫龙辣条",4.5],
    ["老干妈辣酱",20],
]

# 抽奖
# def lottery():
#     print("欢迎抽奖")
#     a = input("输入Y进行抽奖")
#     if a == "y":
#         b = random.randint(1,45)
#         if b <=15:
#             print("机械革命8折优惠券一张")
#             list1 = ["机械革命",0.8]
#         if 15<b <=25:
#             print("洗衣机8这优惠券")
#             list1 = ["洗衣机",0.8]
#         if 25<b<=45:
#             print("卫龙一折优惠券")
#             list1 = ["卫龙辣条",0.5]


# 准备空钱包
money = int(input("初始余额；"))

# 准备空购物车
mycart = []

# 开始购物
i  = 0
print("欢迎抽奖")
a = input("输入Y进行抽奖")
if a == "y":
    b = random.randint(1, 45)
    if b <= 15:
        print("机械革命8折优惠券一张")
        list1 = ["机械革命", 0.8]
    if 15 < b <= 25:
        print("洗衣机8这优惠券")
        list1 = ["洗衣机", 0.8]
    if 25 < b <= 45:
        print("卫龙一折优惠券")
        list1 = ["卫龙辣条", 0.5]
while i < 20:
    for key,value in enumerate(shop):
        print(key,value)
    # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")

    if chose.isdigit():
        chose = int(chose) # "1" --> 1
        if chose > len(shop) or chose < 0: # 9 > 7
            print("该商品不存在！别瞎弄！")
        else:
            if money  > shop[chose][1]:
                if shop[chose][0]==list1[0]:
                    money = money - (shop[chose][1]*list1[1])
                    shop[chose][1]=shop[chose][1]*list1[1]
                    mycart.append(shop[chose])
                    print("本商品优惠",list1[1],"折")
                    print("恭喜，商品添加成功！您的余额为：￥", money)

                else:
                    money = money - shop[chose][1]
                    mycart.append(shop[chose])
                    print("无优惠")
                    print("恭喜，商品添加成功！您的余额为：￥",money)
            else:
                print("温馨提示：您的银行卡余额不足，穷鬼！请买其他商品！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！重新输入！")

    i = i + 1


        # 打印小票
print("以下是您的购物小条，请拿好！！！！么么哒！")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    print(key,value)
print("".center(30,"-"))


# 抽奖
