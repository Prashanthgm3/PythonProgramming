from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title </h1>
<p class="subtitle"> Ipsum Lorem is not understandable </p>
<p> Hello World </p>
<ul>
    <li> Prashanth </li>
    <li> Praveen </li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag)

def find_list_items():
    list_items= simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)

def find_subtitle():
    paragraph = simple_soup.find('p',{'class': 'subtitle'})
    print(paragraph.string)

find_title()
find_list_items()
find_subtitle()