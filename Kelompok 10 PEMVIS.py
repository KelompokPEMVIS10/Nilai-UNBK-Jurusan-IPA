import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Grafik Rerata Nilai UNBK Tingkat SMA Jurusan IPA Se-Indonesia Tahun Ajaran 2018/2019

subjects = ['Matematika', 'Fisika', 'Biologi', 'Kimia', 'Bahasa Inggris', 'Bahasa Indonesia', 'Rerata Nilai Nasional']
y = [38.68, 45.88, 50.03, 50.42, 52.49, 68.07, 52.43]
x = [70, 60, 50, 40, 30, 20, 20, 10]

plt.plot(subjects, y, color='Red', marker='o', label='My Marks')
plt.title("Grafik Rerata Nilai UNBK Tingkat SMA Jurusan IPA Se-Indonesia Tahun Ajaran 2018/2019")
plt.xlabel("Mata Pelajaran")
plt.ylabel("Rata-rata")
plt.grid()
plt.show()