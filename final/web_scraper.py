import requests
import bs4

def scrape(src):
	"""
	Scrape x and y values from online table found at {src}.
	"""
	# use requests (https://2.python-requests.org/en/master/user/quickstart/)...
	# ...to get the required webpage

	r = requests.get(src)
	content = r.text

	# use bs4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) ...
	# ... to parse the page

	soup = bs4.BeautifulSoup(content, 'html.parser')

	# extract the y values
	y_values = soup.find_all(attrs={"class" : "y"})

	for i in range(len(y_values)):
		y_values[i] = int(y_values[i].text)

	# extract the x values
	x_values = soup.find_all(attrs={"class" : "x"})

	for i in range(len(x_values)):
		x_values[i] = int(x_values[i].text)

	return(y_values, x_values)

