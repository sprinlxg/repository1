
# --------------最大值，，求和------------------
# total = 0
# start = 1
# max = 0
# min = 0
# while start <= 10:
#     print("请输入", start, "次分数:")
#     start += 1
#     score = int(input())
#     total += score
#
#
#     if max < score :
#         max = score
#
# print("10名同学总分：",total)
# print("10名同学平均分：",total/10)
# print("最高分：",max)




# -----------------------------计算最大值，平均值等-------------------------
# list = []
# start = 1
# total = 0
# while start <= 10:
#     print("请输入", start, "次分数:")
#     start += 1
#     score = int(input())
#     total += score
#     list.append(score)
#
#
# list.sort()
# print(total)
# print(total/10)
# print(list[0])
# print(list[9])





# 求最小值
# list = [3,4,5,6,7,8,9,10,44,12,555,99,]
# min = list[0]
# for i in list[1:]:
#     if min > i:
#         min = i
# print(min)


# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s' %(i,j,i*j))
#         print()


# 1-100求和
# total = 0
# for i in range(1,101):
#     total += i
# print(total)

# 输出三角形
# for i in range(1,8):
#     for j in range(7-i):
#         print(" ",end = " ")
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print("\n")