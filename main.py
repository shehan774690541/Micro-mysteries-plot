import matplotlib.pyplot as plt

plotCount = 10000

def plotReturn(n = 6):
    sequence = [n]
    while n != 1:
      if n % 2 == 0:
          n //= 2
      else:
          n = 3 * n + 1
      sequence.append(n)
    # print(sequence)
    return sequence


for i in range(1, plotCount + 1):
    plt.plot(plotReturn(i))


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('mathematics loop - shehan774690541')

plt.grid(True)

plt.show()
