# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos
from qutip import *

sz1 = sigmaz()
sz2 = sigmaz()
sx1 = sigmax()
sx2 = sigmaz()
w1 = 1.0*2*pi
w2 = 1.0*2*pi
tlist = np.linspace(0,5,200)
E0 = 10**-3
W = 10**5

psi0 = basis(2,0)
e_ops = [sigmax(), sigmay(), sigmaz()]

H0 = -w1*sz1/2 -w2*sz2/2
H1 =  sx1*sx2
H = [H0,[H1,E0*np.cos(-W*tlist)]]

output = mesolve(H, psi0, tlist, [], e_ops) 

plot_expectation_values(output);


