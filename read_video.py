import time
import os
l=''
while True:
    # 二进制的读取第一行
    with open("E:\\apytemp\\ResponseBody.mp4",'rb') as  f:
        detail=f.readline()
    # 判断是否重复
    if detail==l:
        pass
    else:
        # 判断文件大小是否大于500k
        if os.stat('E:\\apytemp\\ResponseBody.mp4').st_size>500:
            # 以时间设置文件名称
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            # 读文件
            with open("E:\\apytemp\\ResponseBody.mp4", 'rb')as e:
                str = e.read()
            # 换个文件夹存文件
            with open('video\\' + now + ".mp4", "wb") as q:
                q.write(str)
            print("ok")
            time.sleep(0.5)
        else:
            pass
    l = detail
    time.sleep(1)







