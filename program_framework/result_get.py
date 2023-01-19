import os
import shutil
result_dir= r'C:\Users\PC\Desktop\case1_0901\result'  #大文件夹
dir_names = os.listdir(result_dir) # 打开大文件夹后的各个小文件夹名dir_names
final_file='parameter.txt'
for dir in dir_names:  #遍历每一个小文件夹
   file_path = result_dir+'\\'+dir
   file_names = os.listdir(file_path)  #打开小文件夹后每一个CSV文件的名称
   for file in file_names:  #遍历小文件夹里的每一个文件
      file_name = file_path+'\\'+file
      if 'parameter' in file_name:
         print(file_name)
         f=open(file_name).read()
         merge = open(final_file, 'a+')
         merge.write(f)
         merge.close()
from datetime import datetime
time=datetime.now()
timestr=time.strftime("%m.%d.%H.%M")
save_dir=r'C:\Users\PC\Desktop\case1_0901\result'+'\\'+timestr

try:
   if not os.path.exists(save_dir):
      os.mkdir(save_dir)
except:
   print('1')
shutil.move(final_file,save_dir)


