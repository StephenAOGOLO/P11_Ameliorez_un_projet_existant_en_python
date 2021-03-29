from django.core.management.base import BaseCommand
import platform

class Command(BaseCommand):
    print("\nDescription technique de l'environnement informatique ->")
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(info_system()))
        self.stdout.write(self.style.SUCCESS(info_nodename()))
        self.stdout.write(self.style.SUCCESS(info_release()))
        self.stdout.write(self.style.SUCCESS(info_version()))


def info_system():
    return "System : " + str(platform.uname().system)

def info_nodename():
    return "Nodename : " + str(platform.uname().node)

def info_release():
    return "Release : " + str(platform.uname().release)

def info_version():
    return "Version : " + str(platform.uname().version)

