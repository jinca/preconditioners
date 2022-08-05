import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 18.5})


fig = plt.gcf()

fig.set_size_inches(18,10)

valores = [112,224,448,560]

labels = ["112","224","448","560"]

Hypre1 = [214.225,116.725,92.4175,90.8925]

ASM1 = [4188.6,3798.2,2545.5,1365.75]

GAMG = [np.NaN,128.6,68.2,69.7]

#MG1 = [15.25,7.465,5.15,5.052,5.857]

JACOBI1 = [np.NaN,np.NaN,3485.0,3360.0]

BJACOBI1 = [2793.0,1433.0,754.2,633.625]

#plt.plot(valores,Hypre1,marker = "o", color = "b", label ="-pc_type=hypre -pc_hypre_type=boomeramg -ksp_type=cg -ksp_right -pc_factor_shift=NONZERO -snes_type=newtontr -pc_hypre_boomeramg_truncfactor=0.4")
plt.plot(valores,Hypre1,marker = "o", color = "b", label ="hypre boomeramg cg ksp_right factor_shift=NONZERO newtontr truncfactor=0.4")

#plt.plot(valores,ASM1, marker = "d", color = "g", label ="-pc_type=asm -ksp_type=cgs -pc_asm_overlap=32 -snes_type=newtonls -pc_asm_type=interpolate")
plt.plot(valores,ASM1, marker = "d", color = "g", label ="asm cgs overlap=32 newtonls type=interpolate")

#plt.plot(valores,GAMG,marker = "o", color = "c", label ="-pc_type=gamg -ksp_type=cg -pc_factor_shift=NONZERO")
plt.plot(valores,GAMG,marker = "o", color = "c", label ="gamg cg factor_shift=NONZERO")

#plt.plot(valores,MG1,marker = "*", color = "m", label ="-pc_type=mg -ksp_right -ksp_left -ksp_type=bcgs")

#plt.plot(valores,JACOBI1,marker = "d", color = "r", label ="-pc_type=jacobi -ksp_type=tcqmr -ksp_left")
plt.plot(valores,JACOBI1,marker = "d", color = "r", label ="jacobi tcqmr ksp_left")

#plt.plot(valores,SOR1,marker = "p", color = "y", label ="-pc_type=sor -ksp_right -ksp_type=bcgs")

#plt.plot(valores,BJACOBI1,marker = "h", color = "orange", label ="-pc_type=bjacobi -ksp_type=cg -snes_type=newtontr")
plt.plot(valores,BJACOBI1,marker = "h", color = "orange", label ="bjacobi cg newtontr")

#plt.plot(valores,LU1,marker = "d", color = "dodgerblue", label ="-pc_type=lu -ksp_right -ksp_left -ksp_type=bcgs")

plt.xlim(100,566)

#plt.title("Benchmarking of Krylov Subspaces Preconditioned with Preconditioners for Heat Conduction 2D  |  Mesh 1280 x 1280  |  Ten runs")

plt.xlabel("MPI tasks (n)")

plt.ylabel("Execution time (seconds)")

plt.xticks(valores, labels)

plt.legend(loc='upper center', bbox_to_anchor=(0.514, 1.175),
          ncol=1, fancybox=True)
plt.grid()

plt.show()

#plt.savefig("thermal_ksp_1.pdf")
