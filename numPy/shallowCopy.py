import numpy as np
num1 = np.arange(1,6)
print(num1)

num2 = num1.view()
print(num2)

num2 = num2[1]*5
print(num2)