import random
# 接口界面显示
def interface():
    print("#"*40+"\n\n****中国工商银行账户管理系统V1.0****\n\n"+"#"*40)
    option = ["开户","存钱","取钱","转账","查询","BYE"]
    for i in range(1,len(option) + 1):
        print("#",i,".",option[i - 1]," "*27,"#")
    print("#"*40)

# 随机产生8位数字的账户
def account():
    account = ""
    for i in range(1,9) :
        account += str(random.randint(1,9))
    return account

# 地址
def address():
    country = input("国家：")
    province = input("省会：")
    street = input("街道：")
    doorplace = input("门牌：")
    return (country+province+street+doorplace)

# 银行名称
bank_names = ["工商"]
# 银行用户
bank_users = {"工商":[{"账户":"123","密码":"123","姓名":"李明","存款":100},{"账户":"321","密码":"321","姓名":"珍妮","存款":50}]}

# 添加用户
def add_user(user_account,user_name,user_pwd,bank_name):
    if bank_name not in bank_names :
        bank_names.append(bank_name)
        bank_users[bank_name] = [{"账户":user_account,"密码":user_pwd,"姓名":user_name,"存款":0}]
        print(user_name,"开户成功。账户：",user_account)
    else:
        if len(bank_users[bank_name]) > 100 : #?
            print("用户已满。无法申请账户")
        else:
            bank_users[bank_name].append({"账户":user_account,"密码":user_pwd,"姓名":user_name,"存款":0})
            print(user_name, "开户成功。账户：", user_account)
    print(bank_users)

# 银行开户
def open_bank():
    # 账户
    user_account = account()
    # 姓名
    user_name = input("输入姓名：")
    # 密码
    user_pwd = input("输入密码：")
    # 地址
    user_address = address()
    # 开户行名称
    bank_name = input("输入开户行名称：")
    add_user(user_account ,user_name,user_pwd,bank_name)

# 存钱
def save_money():
    account = input("请输入您的账户：")
    money = int(input("存入金额："))
    for i in range(0,len(bank_users["工商"]) ) :
        if account == bank_users["工商"][i]["账户"] :
            bank_users["工商"][i]["存款"] += money
            print(bank_users["工商"][i]["存款"])
            break
        else:
            print("没有该用户。")
            return False

# 取钱
def withdraw_money():
    account = input("输入账户：")
    pwd = input("输入密码：")
    money = int(input("取出金额："))
    for i in range(0,len(bank_users["工商"])):
        if account == bank_users["工商"][i]["账户"]:
            if pwd == bank_users["工商"][i]["密码"]:
                if money < bank_users["工商"][i]["存款"]:
                    bank_users["工商"][i]["存款"] -=money
                    print(bank_users["工商"][i]["存款"])
                    break

                else:
                    print("3")
                    # return 3
            else:
                print("2")
                # return 2
        else:
            print("1")
            # return 1



# 转账
def transfer():
    account1 = input("请输入转入账户：")
    account2 = input("请输入转出账户：")
    money = int(input("请输入装出账户金额："))
    pwd = input("请输入转出账户密码：")
    if account1 in bank_users["工商"][0]["账户"] and account2 in bank_users["工商"][1]["账户"] :
        for i in range(0,len(bank_users["工商"])) :
            if pwd == bank_users["工商"][i]["密码"] :

                if money < bank_users["工商"][i]["存款"] :
                    bank_users["工商"][i]["存款"] -= money
                    print("转出账户存款：",bank_users["工商"][i]["存款"])
                    for j in range(0,len(bank_users["工商"])) :
                        if account1 == bank_users["工商"][j]["账户"] :
                            bank_users["工商"][j]["存款"] += money
                            print("转入账户存款", bank_users["工商"][j]["存款"])


            else:
                print("密码错误。")
                # return 2

    else:
        print("账户不存在。")
        return 1

# 查询
def select():
    account1 = input("查询账户：")
    pwd = input("密码")
    for i in range(0,len(bank_users["工商"])) :
        if account1 in bank_users["工商"][i]["账户"] :
            if pwd == bank_users["工商"][i]["密码"] :
                print(bank_users["工商"][i])
                return 1


            else:
                print("密码错误")

    else:
            print("用户不在")





while True :

    #接口界面显示
    interface()
    q = int(input("办理业务几？\n"))
    if q == 1 :
        open_bank()
        add_user()
    elif q == 2 :
        save_money()
    elif q == 3:
        withdraw_money()
    elif q == 4 :
        transfer()
    elif q == 5 :
        select()
    elif q == 6 :
        pass