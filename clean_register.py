#! /usr/bin/env python
import platform
import os
import sys

def banner():
	print "***********************"
	print "* Reg Clean V 1.0     *"
	print "* Coded by R3BEL10N   *"
	print "* rebelion@riseup.net *"
	print "***********************\n\n"




def check_user():
	if os.getuid() != 0:
			print "[+] Se necesita ser root para ejecutar este script"
			exit()
	else:
		print "[+] Se tienen los permisos necesarios"

class operative():
	def create(self, dirs):
		return os.system('cat /dev/null >> %s' %dirs)
	def remove(self, dirs):
		return os.system('rm %s' %dirs)
	def no_file(self, dirs):
                os.chdir(dirs)
                new = os.getcwd()
                new_logs = os.listdir('%s' %new)
                for a in new_logs:
#                       dir2 = "%s" %new + "%s" %a
                        dir2 = new + "/" +  a
                        print "[*] " + dir2 + " borrado"
                        if os.path.isfile(dir2):
                                self.remove(dir2)
                                self.create(dir2)
                        else:
                                self.no_file(dir2)

class clean():
	op = operative()
	def linux(self):
		logs = os.listdir('/var/log')
		for dirs in logs:
			directs = '/var/log/%s' %dirs

			if os.path.isfile(directs):
				
				op.remove(directs)
				op.create(directs)
				print "[*] " + directs + " borrado"
			else:
				op.no_file(directs)

	def windows(self):
		logs = os.listdir('C:\Windows\System32\winvt\logs\%s')
		for dirs in logs:
			directs = 'C:\Windows\System32\winvt\logs\%s' %dirs

			if os.path.isfile(directs):
				op.remove(directs)
				op.create(directs)
				print "[*] " + directs + " borrado"
			else:
				op.no_file(directs)


if __name__ == '__main__':
	banner()
	cleaner = clean()

	if platform.system() == 'Linux':
		check_user()
		cleaner.linux()

	if platform.system() == 'Windows':
		check_user()
		cleaner.windows()
	else:
		print "[+] Solo implementado para windows y linux"
	
