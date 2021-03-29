from django.core.management import call_command
from pathlib import Path
import time, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def cyclic_dbupdate():
    try:
        now = time.localtime()
        when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
        start_time = when_happens
        print("Lancement de la mise à jour cyclique de la base de données...")
        print("Opération lancée à : {}".format(when_happens))
        call_command('fillDB')
        now = time.localtime()
        when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
        stop_time = when_happens
        print("Fin de la mise à jour cyclique de la base de données...")
        print("Opération terminée à : {}".format(when_happens))
        content = log_content(start_time, stop_time, "Mise a jour de la base de donnees")
        log_it(content=content)
    except Exception as e:
        print(e)


def log_it(path_log="./CRON_LOGS/", filename="cron_event", extension="txt", content=None):
    if content is None:
        content = ["vide\n"]
    os.makedirs(path_log, exist_ok=True)
    now = time.localtime()
    when_happens = "{}-{}-{}_{}-{}-{}".format(now[0], now[1], now[2], now[3], now[4], now[5])
    creation_time = when_happens + "_"
    print("=" * 150)
    new_file = open(path_log + creation_time + filename+"."+extension, "wt")
    for ligne in content:
        new_file.write(ligne)
    new_file.close
    print("le fichier '{}.{}' est prêt".format(filename,extension))


def log_content(start_time, stop_time, event):
    event += "\n"
    return [start_time + " : Debut de " + event, stop_time + " : Fin de " + event]

