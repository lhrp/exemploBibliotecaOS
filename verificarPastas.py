import os
from tkinter import messagebox

pastasCriadas = 0

# Verificar se a pasta 'databases' existe e criá-la se não existir
if not os.path.exists(r'C:\botMakerFiles'):
    os.mkdir(r'C:\botMakerFiles')
    pastasCriadas = 1

if not os.path.exists(r'C:\botMakerFiles\arquivosExcel'):
    os.mkdir(r'C:\botMakerFiles\consumirExcel')
    pastasCriadas = 1
    
if not os.path.exists(r'C:\botMakerFiles\arquivosCSV'):
    os.mkdir(r'C:\botMakerFiles\arquivosCSV')
    pastasCriadas = 1

if not os.path.exists(r'C:\botMakerFiles\img'):
    os.mkdir(r'C:\botMakerFiles\img')
    pastasCriadas = 1

if not os.path.exists(r'C:\botMakerFiles\logs'):
    os.mkdir(r'C:\botMakerFiles\logs')
    pastasCriadas = 1
    
if not os.path.exists(r'C:\botMakerFiles\screenshots'):
    os.mkdir(r'C:\botMakerFiles\screenshots')
    pastasCriadas = 1

if not os.path.exists(r'C:\botMakerFiles\executaveisGerados'):
    os.mkdir(r'C:\botMakerFiles\executaveisGerados')
    pastasCriadas = 1

if not os.path.exists(r'C:\botMakerFiles\scriptsGerados'):
    os.mkdir(r'C:\botMakerFiles\scriptsGerados')
    pastasCriadas = 1


if pastasCriadas == 1:
    messagebox.showinfo("Sucesso", "Pastas bases criadas com sucesso no C:")
else:
    messagebox.showwarning("Atenção", "Pastas já se encontram criadas no C:")