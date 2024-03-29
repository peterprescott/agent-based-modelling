import requests
import bs4

def scrape(src):
    """
    Scrape x and y values from online table found online.
    
    Args:
        src: String representing URL.
    """
    # use requests (https://2.python-requests.org/en/master/user/quickstart/)...
    # to get the required webpage which is intended to be
    # http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html

    scraped_page = requests.get(src)
    content = scraped_page.text

    # use bs4 (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) ...
    # to parse the page
    soup = bs4.BeautifulSoup(content, 'html.parser')

    # extract the x values
    x_values = soup.find_all(attrs={"class" : "x"})

    for i in range(len(x_values)):
        x_values[i] = int(x_values[i].text)

    # extract the y values
    y_values = soup.find_all(attrs={"class" : "y"})

    for i in range(len(y_values)):
        y_values[i] = int(y_values[i].text)

    # why not also extract the z values, in case we want them for something.
    z_values = soup.find_all(attrs={"class" : "z"})

    for i in range(len(z_values)):
        z_values[i] = int(z_values[i].text)

    # and let's return them as coordinate dicts, rather than just as x or y lists.
    scraped_coordinates = []
    for i in range(len(x_values)):
        new_coordinate = {"x":x_values[i], "y":y_values[i], "z":z_values[i]}
        scraped_coordinates.append(new_coordinate)

    return scraped_coordinates
