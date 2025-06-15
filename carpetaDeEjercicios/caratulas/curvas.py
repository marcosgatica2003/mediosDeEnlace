import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datos del problema
Ei = 100  # V/m
alpha = 0.11  # Np/m
beta = 0.032  # rad/m
omega = 2 * np.pi * 150e6  # rad/s
t = 1.67e-9  # s
wavelength = 2 * np.pi / beta  # m
dz = wavelength / 8  # paso de z

# Puntos desde z=0 a z=lambda, cada lambda/8
z_values = np.arange(0, wavelength + dz, dz)

# Cálculos
Ei_exp_alpha = Ei * np.exp(-alpha * z_values)
minus_Ei_exp_alpha = -Ei_exp_alpha
Ex_z_t = Ei * np.exp(-alpha * z_values) * np.cos(omega * t - beta * z_values)

# Crear tabla
table = pd.DataFrame({
    'z (m)': z_values,
    'Ei·e^(-αz) [V/m]': Ei_exp_alpha,
    '-Ei·e^(-αz) [V/m]': minus_Ei_exp_alpha,
    'Ex(z,t) [V/m]': Ex_z_t
})

table_rounded = table.round(3)
table_rounded


# Gráfico de las funciones pedidas
plt.figure(figsize=(10, 6))
plt.plot(z_values, Ei_exp_alpha, label=r'$E_i \cdot e^{-\alpha z}$', color='blue')
plt.plot(z_values, minus_Ei_exp_alpha, label=r'$-E_i \cdot e^{-\alpha z}$', color='red')
plt.plot(z_values, Ex_z_t, label=r'$E_x(z,t)$', color='green')

plt.title('Campo eléctrico Ex(z,t) y envolventes Ei·e^{-αz}, -Ei·e^{-αz}')
plt.xlabel('z (m)')
plt.ylabel('Amplitud del campo eléctrico (V/m)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=0.8)
plt.legend()
plt.tight_layout()
plt.show()

