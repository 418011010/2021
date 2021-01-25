import pandas as pd
from pandas import DataFrame

#读
data = pd.read_excel('1.xlsx')
 
#查看所有的值
print(data.values)
 
#查看第一行的值
print(data.values[0])
 
#查看某一列所有的值
print(data['姓名'].values)
 
#新增列
data['性别'] = None
 
#新增行
data.loc[6] = ['SNOW', 'C', 89, '男']

print(data.values)
#删除行：axis=0
data = data.drop([0], axis=0)
 
#删除列：axis=1
data = data.drop('性别', axis=1)
 
#筛选
rowbool  = data['分数'] < 90
print(data.loc[rowbool])

#排序
data = data.sort_values(by='分数')
print(data.values)

#保存
DataFrame(data).to_excel('1.xlsx', sheet_name='Sheet1', index=False, header=True)

