import matplotlib.pyplot as mpl
import numpy as nmp
import math

batAwal = -5
batAkhir = 8
it = 3

# Graph function
def graph_fct(x):
    y = x**3 + 10*x**2 - 7*x-196
    return y

fig, gp = mpl.subplots()

# Construct graph
def graph_const():
    gp.set_title("Metode Bolzano")
    gp.spines['left'].set_position('zero')
    gp.spines['bottom'].set_position('zero')
    gp.spines['left'].set_color('black')
    gp.spines['bottom'].set_color('black')
    gp.spines['right'].set_color('none')
    gp.spines['top'].set_color('none')
    gp.set_xlabel("X Axis")
    gp.set_ylabel("Y Axis")
    gp.grid()
    return gp

# Graph coordinates
def graph_coord():
    gpX = nmp.linspace(math.floor(batAwal), math.ceil(batAkhir))
    gpY = list(map(graph_fct, gpX))
    gp.plot(gpX, gpY)

# Graph count in bozano
def graph_cntbzn(l, r):
    m = (l + r)/2
    return m

# Create dots on graph
def graph_anim(m, i):
    gp.plot(m, 0, marker = 'o', label = 'Iterasi' + str(i + 1))

# To check bozano
def graph_checkbzn(l, m):
    if(graph_fct(l) * graph_fct(m) > 0):
        return 1
    else:
        return 0

# Graph bozano
def graph_prtbzn(l, r, it):
    for i in range(it):
        m = graph_cntbzn(l, r)
        print("Iterasi " + str(i + 1))
        print("xl = "+ str(l) + "\nxu = "+ str(r) + "\nxr = " + str(m))
        graph_anim(m, i)
        if(graph_checkbzn(l, m)):
            l = m
        else:
            r = m
    print("Aproksimasi x = ", m)

# Run graph
print("Batas awal: " + str(batAwal))
print("Batas akhir: " + str(batAkhir))
print("Jumlah iterasi: " + str(it))
gp = graph_const()
graph_coord()
graph_prtbzn(batAwal,batAkhir, it)
mpl.show()