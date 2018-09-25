import os
import os.path

def createPlatform():
    rootdir = "D:/tiramisu_icomm_duer/components/third_party/dueros_sdk/platform"  # 指明被遍历的文件夹
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # print(parent)
        # print(dirnames)
        for filename in filenames:  # 输出文件信息
            # print(filename[-2:])
            if filename[-2:].__eq__(".c"):
                print("LIB_SRC += "+filename)
            # print("filename is:" + filename)
            # print("the full name of the file is:" + os.path.join(parent, filename))# 输出文件路径信息

def split_fully(path):
    parent,name = os.path.split(path)
    if name == "":
        return (parent,)
    else:
        return split_fully(parent) +(name,)

def createModule():
    # rootdir = "D:/tiramisu_icomm_duer/components/third_party/dueros_sdk/modules/OTA"  # 指明被遍历的文件夹
    rootdir = "D:/tiramisu_icomm_duer/components/third_party/dueros_sdk/external/Zliblite"
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:  # 输出文件信息
            if filename[-2:].__eq__(".c"):
                path = split_fully(parent)
                print("LIB_SRC += " + path[-1] +"/"+filename)
                # print("LOCAL_INC += -I$(MODULE_PATH)/" + path[-1] )


createModule()