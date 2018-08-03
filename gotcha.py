import urllib2, cookielib
import sys
import datetime as dt

class Writer:

	def __init__(self, **kwargs):
		self.content = kwargs.get('content')
		self.hour    = kwargs.get('hour')
		self.minute  = kwargs.get('minute')
		self.second  = kwargs.get('second')

	def save_to_file(self):
		file = "html_{hour}_{minute}_{second}".format(hour=self.hour, minute=self.minute, second=self.second)
		with open(file, "w") as html_file:
			html_file.write(html)



def do_get(req):
	try:
		page = urllib2.urlopen(req)
	except urllib2.HttpError, e:
		print e.fp.read()
	
	content = page.read()
	return content

# do if not exit
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

site = sys.argv[1]
req = urllib2.Request(site, headers=hdr)

html = do_get(req)

now = dt.datetime.now()

writer = Writer(content=html, hour=str(now.hour), minute=str(now.minute), second=str(now.second))
writer.save_to_file()