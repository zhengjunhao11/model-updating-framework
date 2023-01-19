import datetime
import os
import time
from shutil import copy         #shutil 是用来复制黏贴文件的
import numpy as np
#from Identify_modal import Modal_num



def Optimization(x):
    from datetime import datetime
    now = datetime.now()
    timestr = now.strftime("%m.%d.%H.%M.%S_")
    piddir = str(os.getpid())
    file = timestr + '_' + piddir + '_parameter.txt'
    def modify_tcl():
        #if not os.path.exists(piddir):
            #os.mkdir(piddir)
        file_path = r'C:\Users\PC\Desktop\case1_0901\0.6x0.3'      #想拆分的文件路径
        save_dir = r'C:\Users\PC\Desktop\case1_0901\result'   #保存的路径
        try:
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
        except:
            print('direction is not exists')
        pathDir = os.listdir(file_path)         #os.listdir(file_path) 是获取指定路径下包含的文件
        for filename in pathDir:        #检索pathDir下的全部文件的filename
            #print(filename)
            from_path = os.path.join(file_path, filename)   #旧文件的绝对路径（包含文件的后缀名）
            to_path = save_dir + "\\" +piddir            #保存的绝对路径
            if not os.path.isdir(to_path):          #如果 to_path 目录不存在，则创建
                os.mkdir(to_path)
            copy(from_path, to_path)                #完成复制黏贴
        #retval = os.getcwd()                #查看当前工作目录
        #print("当前工作目录为 %s" % retval)    #查看修改后的目录
        work_path=save_dir+'\\'+piddir
        os.chdir(work_path)                      #这是将Python的运行路径修改至pid文件下，否则无法读取其他文件
        #retval = os.getcwd()
        #print("目录修改为 %s" % retval)
        '''
        替换tcl文件内容
        根据文件名替换对应的内容
        '''
        x1 = x[0]*3.75-3.125
        x2 = x[1]*3.75-3.125
        x3 = x[2]*3.75-3.125
        x4 = x[3]*3.75-3.125
        x5 = x[4]*3.75-3.125
        x6 = x[5]*3.75-3.125
        #替换文件
        replace_tcl = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6']
        updating_para = [str(x1), str(x2), str(x3), str(x4), str(x5), str(x6)]
        print('vector', x)
        print('damage', updating_para)
        for i in range(len(replace_tcl)):
            with open('parameter.tcl', 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                f.seek(0)
                for line in lines:
                    if replace_tcl[i] in line:
                        lines = "".join(lines).replace(replace_tcl[i], updating_para[i])
                f.write("".join(lines))
        #end = time.perf_counter()
        #print('duqu:%'%(end - start))
        #Run OpenSEES
        os.system('opensees.exe p.tcl')
        print('finish running os')
        x_input = timestr + ' ' + piddir + ' x ' +str(updating_para)+'\n'
        f=open(file,'a+')
        f.write(x_input)
        f.close()
        time.sleep(2)
        def identify_modal():
            Yshape = timestr + '_yshape.txt'
            Zshape = timestr + '_zshape.txt'
            shape_file = open(Yshape, 'w+')
            shape_file.close()
            n = 10  # n表示一共有n个模态文件需要合并
            for i in range(n):
                for filename in os.listdir():
                    if filename == 'mode' + str(i + 1) + 'y.txt':
                        # print(filename)
                        f = open(filename).read()
                        merge = open(Yshape, 'a+')
                        merge.write(f)
                        merge.close()
                    elif filename == 'mode' + str(i + 1) + 'z.txt':
                        f = open(filename).read()
                        merge = open(Zshape, 'a+')
                        merge.write(f)
                        merge.close()
            Y_simulation = np.array(np.loadtxt(Yshape, dtype=float))  # 读入Y方向所有的振型
            Y_simulation[abs(Y_simulation) < 1e-4] = 0
            Z_simulation = np.array(np.loadtxt(Zshape, dtype=float))  # 读入z方向所有的振型
            Z_simulation[abs(Z_simulation) < 1e-4] = 0
            Target_shape = np.array(np.loadtxt('Target_shape.txt'))
            Y_Target_shape = Target_shape[0:6, ...]
            Z_Target_shape = Target_shape[6:10, ...]
            #print(Z_Target_shape)
            Y_Modal_num = np.zeros(6)
            Z_Modal_num = np.zeros(4)
            # 识别Y方向振型
            for i in range(10):
                row_Y_simulation = Y_simulation[i]
                for j in range(6):
                    cor = np.corrcoef(row_Y_simulation, Y_Target_shape[j, 1:17])
                    Match_level = cor[0, 1]
                    if abs(Match_level) > 0.96 and Y_Modal_num[j] == 0:
                        Y_Modal_num[j] = i + 1
                        break
            # 识别Z方向振型
            for i in range(10):
                for j in range(4):
                    cor = np.corrcoef(Z_simulation[i, ...], Z_Target_shape[j, 1:17])
                    Match_level = cor[0, 1]
                    #print(Match_level)
                    if abs(Match_level) > 0.96 and Z_Modal_num[j] == 0:
                        Z_Modal_num[j] = i + 1
                        break
            #print(Y_Modal_num, Z_Modal_num)
            Modal_num = np.append(Y_Modal_num, Z_Modal_num)
            Modal_num[Modal_num == 0] = 1
            print(Modal_num)
            fre = np.loadtxt('EigenVal.txt', skiprows=1, usecols=3)
            obj_fre = [9.045448e-01,3.469164e+00,8.483372e+00,1.495559e+01,2.414277e+01,3.628435e+01,\
                       4.658184e+00,1.164205e+01,2.455147e+01,3.810883e+01]
            obj_value=0
            for i in range(10):
                if Modal_num[i] !=0:
                    obj_value=obj_value+((fre[int(Modal_num[i]) - 1] - obj_fre[i]) / obj_fre[int(Modal_num[i]) - 1]) ** 2
            print(obj_value)
            fre_file=timestr+'_'+piddir+'_fre.txt'
            os.renames('EigenVal.txt',fre_file)
            obj_input = timestr + ' ' + piddir + ' obj ' + str(obj_value) + '\n'
            f = open(file, 'a+')
            f.write(obj_input)
            f.close()
            os.remove('openSees.exe')
            time.sleep(2)
            return obj_value
        return identify_modal()
    return modify_tcl()

