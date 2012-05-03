#!/usr/sbin/python
#this module will test use of codeigniter cms
import terminal,urllib2
term=terminal.TerminalController()
def check_ci(u):
	try:
			license=urllib2.urlopen(''+u+'license.txt')
			licenseInArray=license.read().split()
			msg=''
			for licenseWord in licenseInArray:
				if licenseWord=='CodeIgniter':
					msg1='\n      CodeIgniter license file :- '+u+'license.txt exists.'
			msg=msg1
			print term.RED+"CodeIgniter: "+term.GREEN+msg
	except:
			pass


