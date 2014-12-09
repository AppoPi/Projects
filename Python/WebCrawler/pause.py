from Tkinter import *
import time
import subprocess

class MyLoop():
	def __init__(self, root):
		#Open website file
		file = open("C:\users\mbuser\Desktop\websites.csv", 'r')
		self.aboutToQuit = False
		self.root = root
		
		while not self.aboutToQuit:
			self.root.update() # always process new events
			#Read in line from file
			try:
				print "Looping"
				webpage = file.readline()
				#Open Chrome to webpage
				p = subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe", webpage])
				#Wait 5 seconds
				time.sleep(5)
				#Kill browser
				p.kill()
				time.sleep(.1)
			except KeyboardInterrupt:
				print '\nPausing...  (Hit ENTER to continue, type quit to exit.)'
				try:
					response = raw_input()
					if response == 'quit':
						sys.exit()
					p.kill()
					print 'Resuming...'
				except:
					print 'Resuming...'
					continue
		
if __name__ == "__main__":
    root = Tk()
    root.withdraw() # don't show the tkinter window
    MyLoop(root)
    root.mainloop()
	
	
	
