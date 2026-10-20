import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('datos_gantt.csv', encoding='utf-8')

df['Fecha_Inicio_Base'] = pd.to_datetime(df['Fecha_Inicio_Base'], format='%d/%m/%Y')
df['Fecha_Fin_Base'] = pd.to_datetime(df['Fecha_Fin_Base'], format='%d/%m/%Y')
df['Fecha_Inicio_Real'] = pd.to_datetime(df['Fecha_Inicio_Real'], format='%d/%m/%Y')
df['Fecha_Fin_Real'] = pd.to_datetime(df['Fecha_Fin_Real'], format='%d/%m/%Y')

df['Duracion_Base'] = (df['Fecha_Fin_Base'] - df['Fecha_Inicio_Base']).dt.days + 1
df['Duracion_Real'] = (df['Fecha_Fin_Real'] - df['Fecha_Inicio_Real']).dt.days + 1
df['Desviacion_Dias'] = (df['Fecha_Fin_Real'] - df['Fecha_Fin_Base']).dt.days

fig, ax = plt.subplots(figsize=(12, 8))

posiciones = range(len(df))

start_base = mdates.date2num(df['Fecha_Inicio_Base'])
ax.barh(posiciones, df['Duracion_Base'], left=start_base, height=0.4, align='edge', color='gray', alpha=0.5, label='Línea Base')

start_real = mdates.date2num(df['Fecha_Inicio_Real'])
colores_real = ['red' if desv > 0 else 'blue' for desv in df['Desviacion_Dias']]
ax.barh([p - 0.35 for p in posiciones], df['Duracion_Real'], left=start_real, height=0.3, align='edge', color=colores_real, alpha=0.8, label='Ejecución Real')

ax.set_yticks(posiciones)
ax.set_yticklabels(df['Id'] + ' ' + df['Nombre'])
ax.invert_yaxis()

ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))

plt.title('Proyecto Alfa Baluarte - Comparativo Línea Base vs Real')
plt.xlabel('Fecha')
plt.ylabel('Actividades')
plt.legend(loc='lower right')
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.savefig('gantt_alfa_baluarte.png')
plt.show()

print(df[['Id', 'Nombre', 'Desviacion_Dias']])