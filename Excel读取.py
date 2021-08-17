import xlrd
wb = xlrd.open_workbook(filename=r"C:\Users\LXG\Desktop\2020年每个月的销售情况.xlsx")
yurong = []
niuzai =[]
fengyi= []
T=[]
majia= []
picao= []
xizhuang=[]
weiyi=[]
qianbiku=[]
chenshan=[]
for i in range(12):
    sa = wb.sheets()[i]
    row = sa.nrows
    col = sa.ncols
    for j in range(row):
        for s in range(col):
            if sa.cell_value(j,s,)=="羽绒服":
                a =sa.row_values(j)
                yurong.append(a)
            elif sa.cell_value(j,s,)=="牛仔裤":
                a = sa.row_values(j)
                niuzai.append(a)
            elif sa.cell_value(j,s,)=="风衣":
                a = sa.row_values(j)
                fengyi.append(a)
            elif sa.cell_value(j,s,)=="T血":
                a = sa.row_values(j)
                T.append(a)
            elif sa.cell_value(j,s,)=="马甲":
                a = sa.row_values(j)
                majia.append(a)
            elif sa.cell_value(j,s,)=="皮草":
                a = sa.row_values(j)
                picao.append(a)
            elif sa.cell_value(j,s,)=="小西装":
                a = sa.row_values(j)
                xizhuang.append(a)
            elif sa.cell_value(j,s,)=="卫衣":
                a = sa.row_values(j)
                weiyi.append(a)
            elif sa.cell_value(j,s,)=="铅笔裤":
                a = sa.row_values(j)
                qianbiku.append(a)
            elif sa.cell_value(j,s,)=="衬衫":
                a = sa.row_values(j)
                chenshan.append(a)

            print(i+1,"月数据",sa.cell_value(j,s),end=" ")
            print()
        print()
sum=0
for d in yurong:
    sum= d[4]+sum
print("羽绒服年销售量：",sum,"件","每件253.6，年销售额：",sum*253.6)
sum1=0
for d in niuzai:
    sum1= d[4]+sum
print("牛仔裤年销售量：",sum1,"件","每件86.3，年销售额：",sum1*86.3)
sum2=0
for d in weiyi:
    sum2= d[4]+sum
print("卫衣年销售量：",sum2,"件","每件253.6，年销售额：",sum2*253.6)
sum3=0
for d in fengyi:
    sum3= d[4]+sum
print("风衣年销售量：",sum2,"件","每件96.8，年销售额：",sum3*96.8)
sum4=0
for d in T:
    sum4= d[4]+sum
print("T学年销售量：",sum2,"件","每件65.8，年销售额：",sum4*65.8)
sum5=0
for d in majia:
    sum5= d[4]+sum
print("马甲年销售量：",sum2,"件","每件49.3，年销售额：",sum5*49.3)
sum6=0
for d in picao:
    sum6= d[4]+sum
print("皮草年销售量：",sum2,"件","每件135.9，年销售额：",sum6*135.9)
sum7=0
for d in xizhuang:
    sum7= d[4]+sum
print("西装年销售量：",sum2,"件","每件494.3，年销售额：",sum7*494.3)
sum8=0
for d in qianbiku:
    sum8= d[4]+sum
print("铅笔裤年销售量：",sum2,"件","每件65.8，年销售额：",sum8*65.8)
sum9=0
for d in chenshan:
    sum9= d[4]+sum
print("衬衫年销售量：",sum2,"件","每件49.3，年销售额：",sum9*49.3)










