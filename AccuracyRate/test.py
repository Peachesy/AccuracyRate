

# 从txt文件读取数据
file_path = r"../AccuracyRateV2/DataFile/6560+80iat_cut_0530_17_45_28.txt"
with open(file_path,encoding='UTF-8') as f:
    # print(f.readlines())
    readed_list = f.readlines()
    print(readed_list)

splited_list = []
for i in readed_list:
    temp=i.split("|")
    print(temp)
    print(f"分割后的数据类型为：{type(temp)}")
    splited_list.append(temp)
print(splited_list)
print(f"新列表的类型：{type(splited_list)}")
