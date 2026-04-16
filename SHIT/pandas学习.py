import numpy as np
import pandas as pd
df1=pd.Series({"小李":"100","小1":"100","小2":"100"})#这里同样有字典的特性，如果你是{"小李":"100","小李":"100","小李":"100"}那么输出是只有——》小李  100
print(df1)
print(df1.iloc[0])#方括号取值，df1.iloc(0)则会被当成函数来调用 <pandas.core.indexing._iLocIndexer object at 0x...>


#dataframe二维数组
M_name=pd.Series(["小李","小吴","小光","小子","雄安绝"])
M_number=pd.Series(['001','002','003','004','005'])
M_score=pd.Series([100,30,50,60,70])
listdf=pd.DataFrame({'name':M_name,'number':M_number,'score':M_score})#很遗憾这里不能加({},->index({})<-这个不能加，可能只有series后可以统一index，如下)
print(listdf)

#作业的写法,dataframe的简单写法？maybe
def create_dataframe():
    '''
    函数功能：创建指定结构的DataFrame并添加新列
    返回值:
    df1: 一个符合要求的DataFrame类型数据，包含指定行列索引和新增列
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    # 1. 构建字典数据，作为DataFrame的基础数据
    # 键为列名（states、pops、years），值为对应列的5行数据 
    dictionary = {
        # 第一列：states，5行数据均为1
        # 第一列：states，5行数据均为1
        'states': [1, 1, 1, 1, 1],
        # 第二列：pops，5行数据均为2
        'pops': [2, 2, 2, 2, 2],
        # 第三列：years，5行数据均为3
        'years': [3, 3, 3, 3, 3] 
    }
    
    # 2. 创建DataFrame对象df1
    # 参数1：字典数据；参数2：index指定行索引为['one','two','three','four','five']
    df1 = DataFrame(dictionary, index=['one', 'two', 'three', 'four', 'five'])
    # 3. 为df1新增列new_add，列值为[7,4,5,8,2]
    # 直接通过列名赋值的方式添加新列，数据长度需与DataFrame行数一致
    df1['new_add'] = [7, 4, 5, 8, 2]
    df1 = df1[['pops', 'states', 'years', 'new_add']]#实现排序
    # ********** End **********#
    # 返回创建并修改后的DataFrame对象
    print(df1)
    return df1



#index来修改索引的值
M_name1=pd.Series(["小李","小吴","小光","小子","雄安绝"],index=["索引1","索引2","索引3","索引4","索引5"])#index要加入等号=才行！！！！
M_number1=pd.Series(['001','002','003','004','005'],index=["索引1","索引2","索引3","索引4","索引5"])
M_score1=pd.Series([100,30,50,60,70],index=["索引1","索引2","索引3","索引4","索引5"])
listdf2=pd.DataFrame({'name':M_name1,'number':M_number1,'score':M_score1})
print(listdf2)


#由于作业写法,所以也可以
listdf=pd.DataFrame({'name':M_name,'number':M_number,'score':M_score},index=["索引1","索引2","索引3","索引4","索引5"
,])
print(listdf)


#导入数据，dataframe直接转换
studenlist={"001":{"姓名":"李专","成绩1":"81","成绩2":"82","成绩3":"83","成绩4":"84"},#记得使用逗号分隔
            "002":{"姓名":"李专","成绩1":"81","成绩2":"82","成绩3":"83","成绩4":"84"},
            "003":{"姓名":"李专","成绩1":"81","成绩2":"82","成绩3":"83","成绩4":"84"},
            "004":{"姓名":"李专","成绩1":"81","成绩2":"82","成绩3":"83","成绩4":"84"},
            "005":{"姓名":"李专","成绩1":"81","成绩2":"82","成绩3":"83","成绩4":"84"}}
print("直接原封不动输出\n",studenlist)
studenlist1=pd.DataFrame(studenlist)
studenlist2=pd.DataFrame(studenlist).T
print("没有转置的\n",studenlist1)#
print("转置的\n",studenlist2)#这个多练！！！！！！！！！！！！


#drop的使用！！
studentlist2_droprow=studenlist2.drop(["002","004"],axis=0)#这里删除了002和004 .drop([索引]，axis=1 or 0) 
print(studenlist2) #这里返回的值不变，可见他不是在原有基础上改，而是获取值改                                               #0为行,1为列
print("删除了行002和004的\n",studentlist2_droprow)
#删除列同理 column列，横栏，栏目
studentlist2_dropcol=studenlist2.drop(["成绩3","成绩4"],axis=1)#1是列，竖着的
print("删除了列成绩3和成绩4的\n",studentlist2_dropcol)


#作业中读取read_csv_data 的作业
def read_csv_data():
    '''
    返回值:
    df1: 一个DataFrame类型数据（存储读取的CSV数据）
    length1: 一个int类型数据（存储DataFrame的总行数）
    '''
    # 请在此添加代码 完成本关任务
    # ********** Begin *********#
    # 1. 读取指定路径的CSV文件，header=0表示以第一行作为列名
    df1 = pd.read_csv('test3/uk_rain_2014.csv', header=0)
    
    # 2. 批量修改df1的列名为指定列表
    new_columns = ['water_year','rain_octsep','outflow_octsep','rain_decfeb','outflow_decfeb','rain_junaug','outflow_junaug']
    df1.columns = new_columns
    """
    这里的df1.colums原本是获取查看列属性的
    但这里刚好用来改列的表头了
    """
    
    # 3. 计算df1的总行数并赋值给length1
    length1 = len(df1)  # 或 df1.shape[0]，效果一致
    
    print(length1)
    print(df1)
    # ********** End **********#
    #返回df1,length1
    return df1, length1


##pandas缺失值的处理：

def demo3():
    import numpy as np
    import pandas as pd
    from sklearn import datasets

    # 加载鸢尾花数据集的特征数据
    iris = datasets.load_iris().data
    #********** Begin **********#
    # 1. 将鸢尾花数据转换为DataFrame，指定列名为a、b、c、d
    df = pd.DataFrame(iris, columns=list("abcd"))
    # 2. 截取前30行数据
    data = df.iloc[:30]  # 切片截取前30行（核心：保证数据范围）
    print("原始数据：\n", data.head(3), "\n")  # 打印前3行预览

    # 3. 每行数据减去第一行对应列的值
    df1 = data - data.iloc[0]  # 按列广播相减，第一行减自身为0
    print("每行减去第一行后的数据：\n", df1.head(3), "\n")

    # 4. 将所有小于0的值替换为缺失值（np.nan）
    df1 = df1.where(df1 >= 0, np.nan)  # 保留≥0的值，<0替换为NaN
    print("替换小于0的值为缺失值后：\n", df1.head(3), "\n")

    # 4.1 检测缺失值：isnull()标记缺失值（True表示缺失）
    null_mask = df1.isnull()  # 缺失值标True，非缺失标False
    print("缺失值掩码（True=缺失）：\n", null_mask.head(3), "\n")

    # 4.2 检测非缺失值：notnull()
    notnull_mask = df1.notnull()  # 非缺失值标True，缺失标False
    print("非缺失值掩码（True=非缺失）：\n", notnull_mask.head(3), "\n")

    # 4.3 统计每行列缺失值数量,按行统计缺失值
    null_count = df1.isnull().sum(axis=1)  # axis=1：按行求和（统计每行缺失值数）
    print("每行缺失值数量：\n", null_count.head(3), "\n")

    # 5. 删除非缺失值数量不足2的行
    df2 = df1.dropna(thresh=2)  # thresh=2：保留至少2个非缺失值的行
    print("删除非缺失值<2的行后：\n", df2.head(3), "\n")

    # 6. 前向填充（ffill）缺失值：用前一行有效值填充
    df3 = df2.fillna(method='ffill')  # ffill=前向填充，NaN用上方有效值替换
    print("前向填充缺失值后的最终结果：\n", df3.head(3))

    #********** End **********#