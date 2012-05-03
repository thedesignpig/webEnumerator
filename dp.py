#!/usr/sbin/python
#this module will test use of Drupal cms 
import terminal,urllib2,re
term=terminal.TerminalController()
def check_dp(u):
		try:
				copyright=urllib2.urlopen(''+u+'COPYRIGHT.txt')
				copyrightInArray=copyright.read().split()			
				msg=''
				for copyrightWord in copyrightInArray:
						if copyrightWord=='Drupal':
							msg1='\n      Drupal copyright file :- '+u+'COPYRIGHT.txt exists.'				
				readme=urllib2.urlopen(''+u+'README.txt')
				readmeInArray=readme.read().split()
				for readmeWord in readmeInArray:
						if readmeWord=='Drupal':
							msg2='\n      Drupal readme file :- '+u+'README.txt exists.'
				
				copyright=urllib2.urlopen(''+u+'modules/')
				f=copyright.read()
				s=re.findall(r"<a \w+=\"\w+", f)				
				mod='\n      Modules :- '
				for i in s:
					mod+=re.findall(r"\w+",i)[2]+','					
				msg=msg1+msg2+mod			
				print term.RED+"Drupal: "+term.GREEN+msg				
				pass
		except:
			pass



