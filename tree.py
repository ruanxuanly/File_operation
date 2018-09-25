import os

src_path = 'D:\YuHen\gushiji'
key = 'HSUART_INT_RX_FIFO_TRIG_LV_16'

def show_dir(path, deep):
    # if deep is 0:
    #     print('.')
    # print('|',end='')
    for node in os.listdir(path):
        if node.__eq__('.svn') or node.__eq__('.vscode'):
            continue
        if node.find('.a')>0:
            continue
        new_path = path + '\\' + node
        if os.path.isdir(new_path):
            show_dir(new_path,deep+1)
        else:
            try:
                fd = open(new_path,'r',encoding='utf-8')
                for i,line in enumerate(fd):
                    if line.find(key) >= 0:
                        print(new_path +'    Line:'+str(i) + '  '+line)
                fd.close()
            except UnicodeDecodeError:
                pass
            except TypeError:
                print(new_path +'encode error')


show_dir(src_path,0)