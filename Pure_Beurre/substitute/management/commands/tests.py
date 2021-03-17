from django.core.management.base import BaseCommand
import subprocess, os

class Command(BaseCommand):
    print("Préparation de la campagne de tests")

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Lancement de la campagne de tests..."))
        try:
            seleniumtestschrome()
            coverage_report()
        except Exception as e:
            print(e)
        self.stdout.write(self.style.SUCCESS("Fin de la campagne de tests..."))

def batch_script():
    subprocess.call([r'start_test.bat'])


def shell_script():
    subprocess.call([r'start_test.sh'])


def all_tests(os_name):
    if os_name == 'nt':
        os.system("coverage run --source='.' manage.py test substitute.project_tester.selenium substitute.project_tester.tests")
    else:
        os.system("coverage run --source='.' ./Pure_Beurre/manage.py test substitute.project_tester.selenium substitute.project_tester.tests")


def units_tests():
    os.system("coverage run --source='.' ./Pure_Beurre/manage.py test substitute.project_tester.tests")


def selenium_tests():
    os.system("coverage run --source='.' ./Pure_Beurre/manage.py test substitute.project_tester.selenium")

def seleniumtestschrome():
    os.system("coverage run --source='.' ./Pure_Beurre/manage.py test substitute.project_tester.selenium.SeleniumTestsChrome")

def coverage_report():
    os.system("coverage html --skip-covered --skip-empty -d substitute\project_tester\coverage_html")


def exit_process():
    os.system("exit&&quit&&q")

