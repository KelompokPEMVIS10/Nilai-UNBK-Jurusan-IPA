import requests
import matplotlib.pyplot as plt
import numpy as np

req = requests.get("https://github.com/muhammadhafizal16/Kelompok10-NilaiUNBK").json()

# Grafik Rerata Nilai UNBK Tingkat SMA Jurusan IPA Se-Indonesia Tahun Ajaran 2018/2019

data_keys = list(req.keys())
data_values = list(req.values())
xdata = np.array(data_keys)
ydata = np.array(data_values)
plt.plot(subjects, y, color='red',marker='o', label='My Marks')
plt.show()