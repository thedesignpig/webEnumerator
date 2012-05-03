#!/usr/sbin/python
#this module will test use of Joomla cms
import terminal,urllib2,re
term=terminal.TerminalController()
def check_joom(u):
		try:
			readme=urllib2.urlopen(''+u+'Readme.txt.txt')			
			f=readme.read()
			s=re.findall(r"Joomla+", f)				
			for i in s:
				msg1='\n      Joomla readme file :- '+u+'Readme.txt.txt exists.'
			msg=msg1
			print term.RED+"Joomla : "+term.GREEN+msg+term.NORMAL
		except:
			pass

