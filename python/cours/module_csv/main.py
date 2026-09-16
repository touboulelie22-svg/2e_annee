# from module_csv import create_folder, create_empty_csv_file, write_to_csv
from module_csv import *

path = "."
folder_name = "data"
filename = "personnes.csv"
colonnes= ['id', 'firstname', 'lastname']

create_folder(path, folder_name)

create_empty_csv_file(
    folder_name,
    filename,
    colonnes= colonnes
)

donnees = [
    {'id': 1, 'firstname': 'John', 'lastname': 'Doe'},
    {'id': 2, 'firstname': 'Alice', 'lastname': 'Smith'},
    {'id': 3, 'firstname': 'Bob', 'lastname': 'Johnson'}
]

write_to_csv(
    path= folder_name,
    filename= filename,
    data= donnees,
    colonnes= colonnes
)