import matplotlib.pyplot as plt
x=[1,2,3,4,5]
e=(0.01,0.01,0.01,0.01,0)
plt.pie(x,explode=e)
plt.title("pie chart")
plt.show()