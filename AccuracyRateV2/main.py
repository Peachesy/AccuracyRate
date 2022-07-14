from Accuracy import *
from ReadTxtData import *
from threading import Thread,Lock


file = r'DataFile/6560+80iat_cut_0530_17_45_28.txt'

# 从TXT读取数据
listdata = ReadTxtData()
listdata.read_txt(file)
# 三家数据
new_data = []
xunfei_data = [i[1] for i in listdata.splited_list][1:]
speech_data = [i[2] for i in listdata.splited_list][1:]
sense_data = [i[3] for i in listdata.splited_list][1:]
# 原始数据
original_query = listdata.original_query[1:len(xunfei_data) + 1]
new_original_query = []
# print("原始数据：", original_query)
# print("讯飞数据：", xunfei_data)
# print("speech数据：", speech_data)
# print("商汤数据：", sense_data)

"""将读取的列表数据写入CSV
第二个参数flag_num是标记厂家的数据，1表示讯飞，2表示思必驰，3表示商汤
xunfei_data = listdata.write_data(1)
固件名称 firmware_version : "HNoise"等
场景名称 scene_name : "55Machine"等
detail：具体噪声信息"""
listdata.write_data(3, "Bank", "HNoise", "7070100")

result = Accuracy()


def run(n,data,num):
    # 把数据写入CSV文件
    listdata.write_data(num, "Bank", "HNoise", "7070100")

    # 申请锁
    lock.acquire()
    print(f"-------------------开始处理{n}的数据-------------------")

    # print("开始线程："+n)
    # 计算距离
    for i in original_query:
        new_original_query.append(list(i))
    # print("new_original_query", new_original_query)
    for j in data:
        new_data.append(list(j))
    # print("new_data", new_data)
    for i, j in zip(new_data, new_original_query):
        result.levenshtein_distance(j, i)
    # 计算参数
    result.process_para_data()
    # 计算WER
    result.wer()
    # 计算CER
    result.ser(original_query,data)
    # print("退出线程："+n)

    # 释放锁
    lock.release()
    print(f"-------------------{n}的数据处理完毕-------------------")
    print()
    print()




if __name__ == '__main__':
    thread_xunfei = threading.Thread(target=run, name="thread_xunfei", args=("Xunfei",xunfei_data,1))
    thread_speech = threading.Thread(target=run, name="thread_speech", args=("Speech",speech_data,2))
    thread_sense = threading.Thread(target=run, name="thread_sense", args=("Sense",sense_data,3))

    # 实例化锁的对象
    lock=Lock()

    # 把子进程设置为守护线程，必须在start()之前设置
    # thread_xunfei.setDaemon(True)
    # thread_speech.setDaemon(True)
    # thread_sense.setDaemon(True)
    thread_xunfei.start()
    thread_speech.start()
    thread_sense.start()

    # 设置主线程等待子线程结束
    thread_xunfei.join()
    thread_speech.join()
    thread_sense.join()
    print("结束")

