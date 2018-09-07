
print("个人所得税计算器\n")
gongzi = int(input("please input your gongzi:"))
qizheng=gongzi-5000
sui = 0
if gongzi<=5000:
    print("不需要缴纳个人所得税！")
elif qizheng<=1500:
    sui = int(qizheng * 0.03)
elif qizheng<=12000:
    sui = int(qizheng * 0.1) - 210
elif qizheng<=25000:
    sui = int(qizheng * 0.2) - 1410
elif qizheng<=35000:
        sui = int(qizheng * 0.25) - 2660
elif qizheng<=55000:
        sui = int(qizheng * 0.3) - 4410
elif qizheng<=80000:
        sui = int(qizheng * 0.35) - 7160
else:
    sui = int(qizheng * 0.45) - 15160
yanglao=gongzi*0.08
yiliao = gongzi * 0.02
gongshang = 0
shengyu = 0
siye = gongzi * 0.005
gongjijin = gongzi * 0.07
print("养老保险", yanglao, "元")
print("医疗保险", yiliao, "元")
print("工伤保险", gongshang, "元")
print("生育保险", shengyu, "元")
print("失业保险", siye, "元")
print("住房公积金",gongjijin,"元")
print("税前工资",gongzi,"元")
print("需要缴纳个人所得税", sui, "元")
print("需要缴纳个人五险",yanglao+yiliao+siye,"元")
print("需要缴纳个人五险一金", yanglao + yiliao + siye + gongjijin, "元")
print("除一金外税后工资", gongzi - sui - yanglao - yiliao - siye, "元")
print("税后工资", gongzi - sui-yanglao-yiliao-siye-gongjijin, "元")