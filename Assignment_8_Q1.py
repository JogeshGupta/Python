import numpy as np
import matplotlib.pyplot as plt

temperature = [42, 45, 47, 50, 53, 49, 56, 60, 54, 48]

arr = np.array(temperature)

print(arr)
print(arr.shape)

print(arr[0])
print(arr[-1])
print(arr[:5])
print(arr[::2])

print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))

updated = arr + 3
print(updated)

above_50 = arr[arr > 50]
print(above_50)
print(len(above_50))

time = np.arange(1, 11)

plt.plot(time, arr, marker='o', label='Original')
plt.plot(time, updated, marker='s', linestyle='--', label='Updated')

plt.title("Robot Motor Temperature")
plt.xlabel("Time Intervals")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid()
plt.show()