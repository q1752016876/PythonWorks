import random

"""
#查看源代码日后爬虫用
import urllib.request

# coding=utf-8

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')

print(data)

# print练手
x = 5 / 2
y = 3 / 2

print('x为', x, '\n', 'y为', y)

print('x和y分别为%.1f,%.1f' % (x, y)) #小数点后留几位

for z in range(1, 11):
    print('{0:5d} {1:5d} {2:4d}'.format(z, z * z, z * z * z))

print("what? ?" + " water")
print(5 + 8)
"""

'''
# if else语句练手
# 猜数字游戏
def numgame():
    Help = '大了'
    Help2 = '小了'
    gmAnswer = 12450
    key = random.randint(1, 10)
    gmAnswer = key
    life = 3

    while life > 0:
        # 防止用户输入异常
        try:    # 尝试直接将输入的str转换成int并赋值
            userAnswer = int(input('随便给个整数\n'))
        except: #并不能转换的场合
            print('你TM给个整数')
            continue

        if userAnswer < gmAnswer:
            print(Help2)
        elif userAnswer > gmAnswer:
            print(Help)
        else:
            print('you win')
            break
        life -= 1
        print('还剩', life, '次机会')
    print('game over')

numgame()
'''

'''
#range配合for的使用
for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)
'''

'''
# 列表使用练习
List = ['pen', 'apple', 'Apple Pen', 12450]
ListCopy = List[:] #不加"[:]"的话如果List变化,那么ListCopy会跟着实时变化
List2 = [9, 'bishi']

print('原来的列表串 ', List)
print('拷贝的列表串: ', ListCopy)
List.pop()
print('pop后', List)
try:
    acarlin = '阿卡林'
    List.remove()
except:
    print('你刚才想删除列表不存在的东西: ', acarlin)

del List[1]  # 删掉下标为1的东西
print(List)
List.append('放肆')  # 加到尾部 append是把一个元素接到列表后面,就算是列表也是作为'一个元素'加到后面
print(List)
List.extend(List2)  # 列表拼接后 extend是把每参数作为列表接到原列表后面
print(List)
List.insert(0, ['插个', '开始'])  # insert(插哪的下标,插啥)   作为一个元素插入
print(List)
'''

'''
# MDZZ题
# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；
# 若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
def stairProblem():
    answer = 1
    while True:
        if answer % 2 == 1 and answer % 3 == 2 and answer % 5 == 4 and answer % 6 == 5 and answer % 7 == 0:
            print('答案是: ', answer)
            break
        else:
            answer += 1


stairProblem()
'''

'''
# 三元互换
x, y, z = 1, 2, 3
print(x, y, z)
x, y, z = y, z, x
print(x, y, z)
'''

'''
# in 资格审查用法
candidate = ['董先生', '马英九', '蔡英文']
if '董' in candidate:
    print('中央已经决定了')
else:
    print('董', '并没有被钦定')

if '董先生' in candidate:
    print('但中央已经决定了董先生')
else:
    print('董', '并没有被钦定')
'''

'''
# 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
chance = 3
password = 'yosha'
while chance > 0:
    userInput = input('输入你的密码')
    if userInput == password:
        print('密码正确')
        break
    elif '*'in userInput:
        print('别输入*号,还剩', chance, '次机会')
        continue
    else:
        chance -= 1
    print('密码错误,还剩', chance, '次机会')
if chance == 0:
    print('错误次数太多')
'''

''''''
# 请问如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
# list1[1][2]= '小鱿鱼'    # 错误,会把列表变成'小鱿鱼'字符串
list1[1][2][0] = '小鱿鱼'  # 正确,变为['小鱿鱼']
print(list1)
