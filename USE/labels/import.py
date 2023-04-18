
#根据挑选的jpg文件找出对应的xml、json、shp、dbf、shx文件
import os
import shutil

filepath1 = 'C:/Users/asd/Desktop/数据集-CPPE/CPPE-TRUE/USE/images/train'#源文件做参考
file_list = os.listdir(filepath1)
print(file_list)
print(len(file_list))

filepath2 = 'C:/Users/asd/Desktop/数据集-CPPE/CPPE-TRUE/USE/labels/train'#需要拷出的文件位置
filepath3 = 'C:/Users/asd/Desktop/数据集-CPPE/CPPE-TRUE/USE/labels/train.1'#拷入新的文件夹
print(len(os.listdir(filepath2)))

def main():
    n=0
    for file in os.listdir(filepath2):
        aa,bb=file.split('x')
        b = aa +'png'
        print(b)
        if b in file_list:
            srcfile = filepath2 +'/'+ file
            dstfile = filepath3 +'/'+ file
            shutil.move(srcfile,dstfile)#剪切功能
            shutil.copyfile(srcfile,dstfile)#拷贝出来
            n=n+1
            print(n)

if __name__ == '__main__':
    main()

