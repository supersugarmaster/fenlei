#-*- coding = utf-8 -*-
#@Time : 2021/5/22 1:51
#@Author : Robert Weng
#@File : fenlei.py
#@Software : PyCharm

'''
思路整理
1.目标：根据提供的关键词，将数据筛选分类，并统计每类的数目
2.流程：
    1)读取待筛选数据：
    方案一：读取excel特定时间段（一周）数据（输入指定时间节点），将该区间往下所有excel内容读取
        评估：可复用性较差，且不比方案二操作上省多少力，否决
    方案二：复制想要筛选的数据，将其粘贴至txt文本中，再读入
        评估：可作用于其他数据，但还是稍显麻烦
    方案三：弹出时间框，选择前后时间段，然后将这段时间内的数据导入
        评估：针对性强，取决于使用者需求
    2)正则匹配：
    读取关键词excel文件，格式为
    xxx:a b c d
    xxx:a b c d
    ...

    将关键词存二重列表list中
    假设待筛选数据为tx
    存放筛选结果dataList
    for i in range(len(list)):
        data = [list[i][0]]
        for j in list[i]
            pattern = re.compile(正则表达式)
            data.extend(pattern.findall(tx))
        dataList.append(data)

    得到的二重列表dataList即包含所有筛选数据，再导出到excel即可



'''