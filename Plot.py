import matplotlib.pyplot as plt
import numpy as np
list_Reward=[
[0.54, 0.59, 0.79, 0.57, 0.38, 0.6, 0.61, 0.55, 0.64, 0.57, 0.65, 0.7, 0.54, 0.41, 0.29, 0.44, 0.62, 0.72, 0.72, 0.62, 0.56, 0.66, 0.71, 0.7, 0.72, 0.74, 0.82, 0.79, 0.69, 0.78, 0.8, 0.81, 0.63, 0.83, 0.85, 0.82, 0.85, 0.88, 0.84, 0.82, 0.78, 0.62, 0.87, 0.83, 0.77, 0.89, 0.81, 0.8, 0.91, 0.74, 0.83, 0.79, 0.76, 0.9, 0.74, 0.86, 0.81, 0.7, 0.89, 0.85, 0.86, 0.82, 0.8, 0.9, 0.86, 0.8, 0.96, 0.92, 0.89, 0.92, 0.75, 0.83, 0.88, 0.77, 0.89, 0.78, 0.82, 0.79, 0.79, 0.78, 0.86, 0.9, 0.92, 0.9, 0.84, 0.73, 0.73, 0.88, 0.88, 0.79, 0.77, 0.84, 0.82, 0.82, 0.8, 0.85, 0.82, 0.86, 0.86, 0.89, 0.87, 0.85, 0.92, 0.87, 0.86, 0.75, 0.81, 0.9, 0.81, 0.85, 0.93, 0.88, 0.8, 0.78, 0.91, 0.88, 0.79, 0.9, 0.8, 0.89, 0.74, 0.74, 0.93, 0.85, 0.86, 0.86, 0.94, 0.93, 0.8, 0.83, 0.87, 0.72, 0.78, 0.87, 0.85, 0.75, 0.82, 0.84, 0.71, 0.79, 0.89, 0.66, 0.78, 0.86, 0.85, 0.86, 0.83, 0.76, 0.68, 0.9],
[0.48, 0.72, 0.48, 0.42, 0.57, 0.71, 0.56, 0.57, 0.68, 0.76, 0.67, 0.79, 0.71, 0.63, 0.69, 0.71, 0.75, 0.74, 0.71, 0.75, 0.77, 0.82, 0.63, 0.8, 0.76, 0.73, 0.83, 0.74, 0.79, 0.71, 0.79, 0.76, 0.69, 0.77, 0.8, 0.91, 0.79, 0.68, 0.78, 0.89, 0.93, 0.86, 0.9, 0.79, 0.79, 0.82, 0.83, 0.88, 0.76, 0.63, 0.77, 0.78, 0.83, 0.78, 0.83, 0.75, 0.8, 0.77, 0.79, 0.66, 0.72, 0.69, 0.87, 0.94, 0.83, 0.77, 0.85, 0.84, 0.8, 0.74, 0.77, 0.65, 0.86, 0.84, 0.84, 0.88, 0.67, 0.8, 0.81, 0.87, 0.76, 0.81, 0.87, 0.72, 0.92, 0.74, 0.89, 0.87, 0.88, 0.72, 0.77, 0.88, 0.8, 0.74, 0.85, 0.88, 0.79, 0.82, 0.82, 0.89, 0.79, 0.82, 0.89, 0.87, 0.84, 0.81, 0.78, 0.58, 0.77, 0.88, 0.85, 0.85, 0.9, 0.84, 0.76, 0.86, 0.86, 0.79, 0.82, 0.81, 0.77, 0.86, 0.84, 0.83, 0.86, 0.73, 0.85, 0.84, 0.86, 0.85, 0.78, 0.8, 0.85, 0.89, 0.84, 0.86, 0.82, 0.79, 0.93, 0.8, 0.89, 0.8, 0.8, 0.78, 0.77, 0.79, 0.85, 0.9, 0.87, 0.88],
[0.67, 0.46, 0.6, 0.6, 0.59, 0.64, 0.67, 0.54, 0.39, 0.64, 0.69, 0.65, 0.64, 0.71, 0.63, 0.61, 0.68, 0.72, 0.86, 0.59, 0.8, 0.74, 0.79, 0.74, 0.66, 0.87, 0.78, 0.7, 0.62, 0.74, 0.85, 0.81, 0.76, 0.84, 0.86, 0.82, 0.89, 0.76, 0.71, 0.79, 0.79, 0.92, 0.88, 0.93, 0.84, 0.85, 0.85, 0.85, 0.8, 0.9, 0.84, 0.81, 0.84, 0.74, 0.68, 0.89, 0.75, 0.85, 0.89, 0.81, 0.88, 0.77, 0.81, 0.89, 0.82, 0.82, 0.78, 0.82, 0.9, 0.72, 0.8, 0.83, 0.79, 0.86, 0.82, 0.82, 0.8, 0.82, 0.8, 0.72, 0.91, 0.75, 0.79, 0.77, 0.86, 0.88, 0.92, 0.88, 0.8, 0.72, 0.71, 0.78, 0.89, 0.82, 0.91, 0.88, 0.69, 0.72, 0.85, 0.84, 0.82, 0.8, 0.82, 0.87, 0.82, 0.78, 0.8, 0.81, 0.86, 0.87, 0.85, 0.85, 0.88, 0.87, 0.86, 0.7, 0.83, 0.71, 0.81, 0.89, 0.72, 0.74, 0.82, 0.82, 0.89, 0.77, 0.84, 0.76, 0.79, 0.78, 0.8, 0.74, 0.93, 0.91, 0.81, 0.91, 0.77, 0.83, 0.82, 0.79, 0.85, 0.84, 0.87, 0.8, 0.78, 0.79, 0.82, 0.8, 0.79, 0.78]
]
mu_reward = np.mean(list_Reward, axis=0)
std_reward = np.std(list_Reward, axis=0)
number_of_steps=len(list_Reward[0])
time = np.arange(1, number_of_steps + 1, 1.0)
time=np.arange(1, number_of_steps + 1, 1.0)
plt.plot(time, mu_reward, color='green')#, label='Mean Reward')
plt.grid()
plt.show()
''''
plt.fill_between(time, mu_reward-std_reward, mu_reward+std_reward, facecolor='blue', alpha=0.3)
#plt.legend(loc='upper right')
plt.xlabel('Steps')
plt.ylabel('Reward')
plt.title('Spectrogram')
file_name = 'Spectrogram.png'
plt.savefig('./Learning_Curves/'+file_name)
plt.show()
'''