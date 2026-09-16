import os
import pandas
import csv
def create_folder(path, name):
    chemin = os.path.join(path, name)
    if not os.path.exists(chemin):
        os.mkdir(chemin)
    else:
        print("le chemin existe deja")


path = ".."
name = "test"
create_folder(path, name)
