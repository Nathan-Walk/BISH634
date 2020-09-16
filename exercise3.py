import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=3
h=np.logspace(-10,0)
y=(((x+h)**3-(x**3))/h)-27


plt.style.use('ggplot')
plt.loglog(h,y)


plt.xlabel("h")
plt.ylabel("Difference")
plt.show()
