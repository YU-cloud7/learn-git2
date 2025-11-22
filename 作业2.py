#####列表
my_list=[1,2,3,4,5,6,"sun"]
##查询
print(my_list[0])
##修改
my_list[3]="rainy"
print(my_list)
##插入
my_list.insert(1,'wind')
print(my_list)
##删除
my_list.remove(5)
print(my_list)
##添加
my_list.append("cloud")
print(my_list)

#####元组
tuple=(1,'apple',2,3,'banana','apple')
##查询
try:
    index =
tuple.index('apple')
    print("'apple'第一次出现的下标:",index)
except ValueError:
    print('元素不存在')
##统计
apple_count=
tuple.count('apple')
print("'apple'出现次数："，apple_count)
#####字典
studen_scores={
    'Alice':85,
    'Bob':92,
    'Charlie':78,
    'Diana':96
}
## 添加元素
student_scores['Eve'] = 88
print("添加Eve后:", student_scores)

# #修改元素
student_scores['Charlie'] = 82
print("修改Charlie分数后:", student_scores)

# 删除元素
del student_scores['Bob']
print("删除Bob后:", student_scores)

# 遍历字典
print("\n遍历字典:")
print("学生姓名和分数:")
for name, score in student_scores.items():
    print(f"{name}: {score}")

print("\n只遍历键:")
for name in student_scores.keys():
    print(name)

print("\n只遍历值:")
for score in student_scores.values():
    print(score)
#####集合
# 创建两个列表
list1 = [1, 2, 3, 4, 5, 2, 3]
list2 = [4, 5, 6, 7, 8, 4]

print("列表1:", list1)
print("列表2:", list2)

# 转换为集合
set1 = set(list1)
set2 = set(list2)

print("集合1:", set1)
print("集合2:", set2)

# 计算交集
intersection = set1 & set2  
print("交集:", intersection)

# 计算并集
union = set1 | set2 
print("并集:", union)

