#!/usr/sbin/python
#scan websites to check what's used to make the website
import sys,os,socket,subprocess,urllib2,urlparse,terminal
import wp,dp,ci,joom,oc
#urldefrag
term=terminal.TerminalController()
url=""
def main():
	if len(sys.argv)==1:
		usage()
	else:
		url=sys.argv[1]		
		if urllib2.urlopen(''+url+'').getcode()==200:
			urlParsed=urlparse.urlparse(''+url+'')
			#urlDefragmented=urldefrag(''+url+'')
			indexOpen=urllib2.urlopen(''+url+'')			
			print term.RED+"Server :"+term.GREEN+indexOpen.info()['Server']
			wp.check_wp(''+url+'')
			dp.check_dp(''+url+'')
			ci.check_ci(''+url+'')
			joom.check_joom(''+url+'')
			#oc.check_oc(''+url+'')					
def usage():
	print term.GREEN+"Website Scan v0.1 alpha\nUsage: "
	print term.RED+sys.argv[0]+" url"+term.NORMAL
	#print sys.argv[0]+" url"+" proxy"
def banner():
	print ""


if __name__=="__main__":
	main()
