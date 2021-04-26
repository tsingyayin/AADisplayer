#在我把窗体里面，尤其是PyQt下的编写整明白之前，
#先用这个工程完成基本的标准化剧情文件处理测试。
import sys
sys.path.append(r"C:\Users\Administrator\source\repos\PlayerCore\PlayerCore")
import core 

programme_end=0
while programme_end==0 :
    Storyname=input("请输入剧情文件名称（直接回车，现在固定测试N2.spol这个文件）")
    Storyname="N2.spol"
    files=open(Storyname,"r")
    Ver=""

#用来确认遵循版本号
    for line in files.readlines():
        if (line[0]=="#" and line[0:3]!="###") or line[0]=="\n" or line[0]==" ":continue
        elif line[0]=="/": 
                Ver=line[1:-1]
                break#用break节省时间
    print("文档的版本是",Ver)



#重新打开文件，从头开始处理
    files=open(Storyname,"r")

    if Ver=="SPOL0.2":                                                         #遵循SPOL0.2标准的读取
        core.SPOL0_2(files)

    elif Ver=="SPOL0.2.5":                                                    #遵循SPOL0.2.5标准的读取
        core.SPOL0_2_5(files)

    else:
        print("没有在解释器中找到{}这个版本，请检查拼写，或者检查本版程序是否支持这个版本".format(Ver))
        print("解释器内曾把所有的AASD，AASP前缀全部替换成了SPOL，请检查您的前缀是否为SPOL")


    files.close()
    print("剧情文件读取完毕")
    input("按下回车重新读取")