# Model-updating-framework
:bulb: A program framework suitable for model updating of complex structures based on parallel computing.

:loudspeaker: Introduce
=====
Based on the open-source software OpenSees and Python, a program framework suitable for the model updating of complex structures was proposed. Firstly, an efficient parallel optimization algorithm for FE model updating (FEMU) of complex civil structures was developed in Python. Then, the program interfaces were developed to link the model analysis module and the parallel computing module to realize the parallel analysis and FEMU of complex structures. On this basis, the damage identification of a simply supported beam was taken as an example to validate the feasibility and accuracy of the program framework.

:memo: Install
========
Download the file that includes the **simply supported beam(TCL file)** and **program framework code**.


:memo: Framework Components
========
:wrench: `Input.py`: define algorithm parameters, upper and lower bounds for normalization parameters, and set up parallel computing environment of Windows.

:wrench: `Parallel.py`: call the multiprocessing to create a Pool required for parallel computing to realize parallel computing of optimization algorithms.

:wrench: `Optimization.py`: through the three functions **Modify_tcl()**, **Run_OpenSees()** and **Objective_function()** respectively realize the parameter correction, calculation analysis and objective function value calculation of the structural model.

:wrench: `PSO.py`, or(`GA.py` and `operators`): based on the sko developed by guofe9778: https://github.com/guofei9987/scikit-opt

:wrench: `result_get.py`: Process updating results

:memo: Start
========
**_Run the Input.py_**
