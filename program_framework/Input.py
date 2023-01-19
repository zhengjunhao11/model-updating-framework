import os
from multiprocessing import freeze_support,set_start_method
import multiprocessing
from Optimization import Optimization
from GA import RCGA
from PSO import PSO

if __name__=='__main__':
    from datetime import datetime
    start = datetime.now()
    print('start:', start.strftime("%m.%d.%H.%M"))
    multiprocessing.freeze_support()
    lower = [0.9, 0.9, 0.9,0.9,0.9,0.9]
    upper = [1.1,1.1,1.1,1.1,1.1,1.1]
    pso = PSO(func=Optimization, n_dim=6, pop=72, max_iter=30, w=0.8, lb=lower, ub=upper, c1=1.49, c2=1.49,verbose=True)
    #freeze_support()
    #set_start_method('forkserver')
    pso.record_mode=True
    pso.run(precision=1e-5)
    print('best_x',pso.pbest_x,'\n','best_y',pso.pbest_y)
    f =open('best_opt.txt','a+')
    f.write(str(pso.best_x))
    f.close()
    f=open('updating_processing.txt','a+')
    f.write(str(pso.pbest_x))
    f.write('\n')
    f.write(str(pso.pbest_y))
    end=datetime.now()
    print('end',end.strftime("%m.%d.%H.%M"))
    os.system('MAC.py')