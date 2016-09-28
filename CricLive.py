from bs4 import BeautifulSoup
import urllib2, pynotify

while True:
	request = urllib2.Request('http://www.espncricinfo.com/ci/engine/match/index.html?view=live')
	request.add_header('User-agent', 'Mozilla/5.0')
	open = urllib2.urlopen(request)
	page = BeautifulSoup(open, 'html.parser')
	pynotify.init("Display")
	p1= page.find(id="live-match-data")
	p2= p1.find("section",{"class":"matches-day-block"}).text
	notice=pynotify.Notification("cricket Live",p2)
	notice.show()
