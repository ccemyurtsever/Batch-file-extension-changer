import os
import time


# Gui arayüz yapılacak Pyqt5
folder_path = "C:\\xxx\\xxx\\xxx\\xxx" # değiştirilecek klasör yolu
old_ext = ".txt"  # Eski uzantı
new_ext = ".md"  # Yeni uzantı


awser = str(input())
def areYouSure(awser):
    if awser.lower() == "yes":  
        for filename in os.listdir(folder_path):
            if filename.endswith(old_ext):
                new_name = os.path.splitext(filename)[0] + new_ext
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
    else:
        pass



