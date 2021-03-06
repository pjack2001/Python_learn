#此脚本用python3所写，win7上跑的
#目的是实现把图片放入一个指定文件夹， 即可开始打印的，自动打印功能软件
#实现类似景区的自动照片打印功能， 目前暂时不带http上传功能。
#此脚本用到了图片软件IrfanView32,请先自行下载安装， 并把安装路径加入系统path.,其实本质是由i_view32来触发打印。进入infraview的安装目录，把i_view32.exe复制到当前脚本所在文件夹
#双击打开i_view32，并打开一张图片，选择打印，设定好各种打印参数， 选择保存在save current dialog settings
#本脚本调用默认打印机，请先行把默认打印机的纸张，打印质量等设好，另外加入水印功能可以从打印机的设定里搞定，另外，我的打印机是爱普生R330，连供版。
import os,time
def check_config(filename):
    mode=os.path.isfile(filename)
    return mode
def check_pic():
    #检查当前文件夹有没有jpg后缀的图片
    for pic in os.listdir():
        if pic.endswith('.jpg') or pic.endswith('.JPG'):
            print (pic)
            printing_del_pic(pic)
def printing_del_pic(img):
    #先打印，后删除
    os.system('i_view32.exe '+img+' /print')
    os.remove(img)
    
def main():
    if__loop()

def core():
    
    #先查看有没有IrfanView32，i_view32.exe有没有在当前目录
    if check_config('i_view32.exe'):
        print ('config ok')
        check_pic()
        #再检查有没有图片
        #printing()
        #打印图片
        #rm_pic()
        #删除图片
    else:
        print ('Error:i_view32.exe not in this folder, please install IrfanView32, and copy i_view32.exe to current folder')
def if__loop():
    loop=1
    #True是循环，False为单次
    if loop:
        while True:
            core()
            time.sleep(30)
            #循环间隔时间
    else:
        core()
    
if __name__=="__main__":
#主函数
    main()
