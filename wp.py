#!/usr/sbin/python
#this module will test use of wordpress cms
import terminal,urllib2
term=terminal.TerminalController()
licenseWord=''
def check_wp(u):
	try:
		license=urllib2.urlopen(''+u+'license.txt')
		licenseInArray=license.read().split()
		msg=''
		for licenseWord in licenseInArray:
			if licenseWord=='WordPress':
				msg1='\n      Wordpress license file :- '+u+'license.txt exists.'
		readme=urllib2.urlopen(''+u+'readme.html')
		readmeInArray=readme.read().split()
		for readmeWord in readmeInArray:
			if readmeWord=='WordPress':
				msg2='\n      Wordpress readme file :- '+u+'readme.html exists.'
		version=urllib2.urlopen(''+u+'')
		theme=urllib2.urlopen(''+u+'')
		count=0
		while(count<11):
			count=count+1
			tmp=theme.readline()
		theme=theme.readline()
		themeInArray=theme.split()
		theme=themeInArray[2]
		theme=theme.split('/')
		theme=theme[6]
		msg3='\n      Wordpress theme in use is :- '+theme
		msg=msg1+msg2+msg3
		print term.RED+"Wordpress: "+term.GREEN+msg+term.NORMAL
	except:
		pass		

