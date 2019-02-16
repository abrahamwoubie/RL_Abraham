import matplotlib.pyplot as plt
import numpy as np
list_Reward=[
[0.00,0.40,0.50,0.22,0.25,0.57,0.44,0.25,0.22,0.50,0.45,0.22,0.30,0.36,0.33,0.56,0.33,0.45,0.30,0.12,0.55,0.33,0.33,0.30,0.58,0.69,0.62,0.44,0.64,0.56,0.71,0.67,0.76,0.75,0.81,0.50,0.73,0.82,0.95,0.80,0.89,0.85,0.73,0.90,0.82,0.73,0.76,0.64,0.85,0.78,0.83,0.74,0.81,0.88,0.69,0.83,0.88,0.64,0.78,0.76,0.89,0.88,0.90,0.82,0.79,0.58,0.90,0.90,0.73,0.95,0.94,0.76,0.83,0.88,0.83,0.83,0.69,0.71,0.89,0.67,0.85,0.94,0.69,0.88,0.79,0.89,0.75,0.87,0.80,0.69,1.00,0.82,0.85,0.81,0.83,0.87,0.88,0.86,0.95,0.88,0.93,0.95,0.95,0.85]
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