import os
import os.path
str_src = "C:/Users/Xuan/Downloads/Duer_Light_Profile_6786"

for parent,dirs,names in os.walk(str_src):
    for name in names:
        if name[-4:].__eq__('_str'):
            # os.remove(os.path.join(parent,name))
            continue
        fd = open(os.path.join(parent,name))
        fd_new = open(os.path.join(parent,name)+'_str','w')
        print('// char *profile_buf = "'+fd.readline().replace('\"','\\\"')+'";')
        fd_new.write(fd.readline().replace('\"','\\\"'))
        fd.close()
        fd_new.close()