import librosa
import pandas as pd
import numpy as np

archivo = "nombre_de_archivo_de_audio.mp3" 

inicio_segundo = 124  # multiplicar los minutos por sesenta y luego sumar por segundos
fin_segundo = 127  # multiplicar los minutos por sesenta y luego sumar por segundos

duracion_total = fin_segundo - inicio_segundo

y, sr = librosa.load(archivo, offset=inicio_segundo, duration=duracion_total, sr=22050)
tiempo = np.linspace(0, len(y) / sr, len(y))

df = pd.DataFrame({
    'tiempo_en_segs': tiempo,
    'amplitud': y
})

df.to_csv("dataset_de_los_3_segundos_elegidos.csv", index=False, decimal='.')
