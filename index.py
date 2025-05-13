import json
import matplotlib.pyplot as plt

# Cargar los datos
with open('temperaturas.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# Extraer los datos
meses = [item['mes'] for item in datos['temperaturas']]
minimas = [item['minima'] for item in datos['temperaturas']]
maximas = [item['maxima'] for item in datos['temperaturas']]
promedios = [(min_ + max_) / 2 for min_, max_ in zip(minimas, maximas)]

# Crear la gráfica
plt.figure(figsize=(12, 6))

plt.plot(meses, minimas, marker='o', label='Temperatura Mínima (°C)', color='blue')
plt.plot(meses, maximas, marker='o', label='Temperatura Máxima (°C)', color='red')
plt.plot(meses, promedios, marker='o', linestyle='--', label='Temperatura Promedio (°C)', color='green')

# Personalización
plt.title('Temperaturas Mínimas, Máximas y Promedio por Mes')
plt.xlabel('Mes')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

# Mostrar
plt.show()
