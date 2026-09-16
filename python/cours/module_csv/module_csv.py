import os
import pandas
import csv


__all__ = [
    'create_folder',
    'create_empty_csv_file',
    'write_to_csv'
]


def create_folder(path, name):
    chemin = os.path.join(path, name)
    if not os.path.exists(chemin):
        os.mkdir(chemin)
    else:
        print(f"Attention ! Le dossier '{name}' existe déjà !")


def create_empty_csv_file(path: str, filename: str, /, *, colonnes: list, separator= ','):
    filename = _sanitize_filename(filename)
    if not filename.endswith('.csv'):
        liste = filename.split('.') # exemple ['donnees', 'txt']
        filename = liste[0] + '.csv'

    chemin = os.path.join(path, filename)
    if os.path.exists(chemin):
        return

    tableau = pandas.DataFrame(columns= colonnes)
    tableau.to_csv(chemin, sep= separator, index= False)



def write_to_csv(path: str, filename: str, data: list[dict], colonnes: list[str], separator= ','):
    if not filename.endswith('.csv'):
        liste = filename.split('.')
        filename = liste[0] + '.csv'
    chemin = os.path.join(path, filename)
    if not os.path.exists(chemin):
        return

    with open(chemin, 'a') as fichier:
        writer = csv.DictWriter(fichier, colonnes, delimiter= separator, lineterminator= '\r')
        writer.writerows(data)


def _sanitize_filename(filename: str) -> str:
    return filename.strip().replace(' ', '_')