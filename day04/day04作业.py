# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))

# li.append('seven')
# print(li)

# li.insert(0,'tony')
# print(li)

# li[1]="Kelly"
# print(li)

# li.extend([1,"a",3,4,"heart"])
# print(li)

# li.extend("qwert")
# print(li)

#请删除列表中的元素"ritian",并输出添加后的列表
# li.pop(2)
# print(li)

# 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# print(li.pop(1))
# print(li)

#请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)

#2利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# print(li[:3])
# print(li[3:6])
# print(li[:7:2])
# print(li[1:6:2])
# print(li[-1])
# print(li[-3:-8:-2])


# lis = [2, 30, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# ll=lis[3][2][1][0].upper()
# lis[3][2][1][0]=ll
# print(lis)

# lis[3][2][1][0]='TT'
# print(lis)

# lis[3][2][1][1]='100'
# print(lis)
# lis[3][2][1][1]=str(lis[3][2][1][1]+97)
# print(lis)


# lis[3][2][1][2]=101
# print(lis)
# lis[3][2][1][2]=int(lis[3][2][1][2])+100
# print(lis)

#利用下划线将列表的每一个元素拼接成字符串"alex_wusir_taibai"
# li = ["alex", "wusir", "taibai"]
# ll='_'.join(li)
# print(ll,type(ll))

#利用for循环和range打印出下面列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)

#6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
# ll=[]
# for i in range(2,101,2):
#     ll.append(i)
# print(ll)

#7.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中
# ll=[]
# for i in range(51):
#     if i % 3==0:
#         ll.append(i)
# print(ll)

#利用for循环和range从100~1，倒序打印。
# for i in range(100,0,-1):
#     print(i)


ll=[]
for i in range(100,9,-1):
    ll.append(i)
print(ll)









