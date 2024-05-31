import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi Riemann
def riemann_integral(f, a, b, N):
    width = (b - a) / N
    total_area = 0
    for i in range(N):
        total_area += f(a + i * width) * width
    return total_area

# Fungsi untuk menghitung galat RMS
def rms_error(estimated, actual):
    return np.sqrt(np.mean((estimated - actual) ** 2))

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N yang dapat dipilih
N_values = [10, 100, 1000, 10000]

while True:
    print("\nPilih nilai N dari opsi berikut:")
    for i, N in enumerate(N_values, start=1):
        print(f"{i}. {N}")
    print("5. Keluar")

    # Minta input dari pengguna
    choice = int(input("Masukkan pilihan (1-5): "))

    # Validasi input
    if 1 <= choice <= 4:
        N = N_values[choice - 1]
        start_time = time.time()
        pi_estimate = riemann_integral(f, 0, 1, N)
        end_time = time.time()
        execution_time = end_time - start_time
        error = rms_error(pi_estimate, pi_reference)
        
        print(f'\nHasil untuk N = {N}')
        print(f'Pi Estimate: {pi_estimate}')
        print(f'RMS Error: {error}')
        print(f'Execution Time: {execution_time} seconds')
    elif choice == 5:
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
