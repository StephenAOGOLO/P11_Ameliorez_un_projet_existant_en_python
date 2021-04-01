""" This module is a manage.py command
 used for update the website database.  """
from django.core.management.base import BaseCommand
from django.core.management import call_command
from pathlib import Path
import time, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Command(BaseCommand):
    """ This class is getting ready the user """
    print("\n")
    print("=" * 150)
    print("Préparation de la mise à jour automatique")

    def handle(self, *args, **options):
        """  This method runs the following actions:
            - To display operating system details
            - To display the total quantity of aliments
            - To update database
        """
        self.stdout.write(self.style.SUCCESS("Lancement de la mise à jour automatique..."))
        try:
            call_command('environs')
            call_command('all_aliments')
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
            call_command('all_aliments')
        except Exception as e:
            print(e)
        self.stdout.write(self.style.SUCCESS("Fin de la mise à jour automatique..."))
        print("=" * 150+"\n")


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