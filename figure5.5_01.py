from idlelib.idle_test.test_browser import f1, f2
from typing import Optional, Union, Tuple

import matplotlib.pyplot as plt
import numpy as np
from numpy.core._multiarray_umath import ndarray

plt.figure()  # Make separate figures
plt.subplot(2, 1, 1)
t = np.linspace(0, 3, 51)
y1 = f1(t)
y2 = f2(t)

plt.plot(t, y1, '-r', t, y2, 'bo')
plt.xlabel('t')
plt.ylabel('y')
plt.axis([t[0], t[-1], min(y2)-0.05, max(y2)+0.5])
plt.legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)'])
plt.title('Top figure')

plt.subplot(2, 1, 2)
t3 = t[::4]
y3 = f2(t3)

plt.plot(t, y1, 'b-', t3, y3, 'ys')
plt.xlabel('t')
plt.ylabel('y')
plt.axis([0, 4, -0.2, 0.6])
plt.legend(['t^2*exp(-t^2)', 't^4exp(-t^2)'])
plt.savefig('tmp4.pdf')
plt.show()
