import subprocess
import os
import platform
from tools.colors import Colors

class SceSetupTool:
    os = ""
    color = Colors()

    def check_installation(self, name, command, link):
        devnull = open(os.devnull, 'wb')
        software = subprocess.check_call(command, stdout=devnull, stderr=subprocess.STDOUT)
        if software == 0:
            self.color.print_yellow(name + " found", True)
        else:
            self.color.print_red(name + " not found", True)
            print("visit here to install: ")
            self.color.print_purple(link, True)
            print("press enter to continue: ")
            choice = input()
            while choice != "":
                choice = input()

    def check_os(self):
        self.os = platform.system()
        self.color.print_purple(self.os, True)

    def check_directory(self, name):
        if os.path.isdir(name):
            os.chdir(name)
            devnull = open(os.devnull, 'wb')
            if os.system("git diff-index --quiet HEAD") == 0:
                self.color.print_pink("Work found please check changes first", True)
            else:
                os.system("git checkout master")
                os.system("git fetch origin")
                os.system("git reset --hard origin/master")
            os.chdir("..")
        else:
            os.system("git clone https://github.com/SCE-Development/" + name)
            os.system("cd " + name)

    def setup_rpc(self):
        if os.path.isdir("sce-rpc"):
            os.chdir("sce-rpc")
            devnull = open(os.devnull, 'wb')
            subprocess.check_call("git checkout master", stdout=devnull, stderr=subprocess.STDOUT)
            subprocess.check_call("git fetch origin", stdout=devnull, stderr=subprocess.STDOUT)
            subprocess.check_call("git reset --hard origin/master", stdout=devnull, stderr=subprocess.STDOUT)
            os.chdir("..")
        else:
            os.system("git clone https://github.com/SCE-Development/sce-rpc")
            if self.os == "Windows":
                os.system("setup.bat")
            else:
                os.system("setup.sh")