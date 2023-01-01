import os
import glob
import py2exe

# Klasörleri oluşturma
if not os.path.exists('input'):
    os.makedirs('input')
if not os.path.exists('output'):
    os.makedirs('output')

# Input klasöründeki .py dosyalarını listeleme
py_files = glob.glob('input/*.py')

# Dosyaları listeleme
for i, file in enumerate(py_files):
    print(f'{i+1}: {file}')

# Kullanıcıdan dosya seçimi
selected_file = int(input('Lütfen bir dosya seçin: '))
selected_file = py_files[selected_file - 1]

# exe dosyasını oluşturma
py2exe.convert(selected_file, 'output/' + os.path.splitext(os.path.basename(selected_file))[0] + '.exe')
print(f'{selected_file} dosyası output klasörüne exe olarak kaydedildi.')
