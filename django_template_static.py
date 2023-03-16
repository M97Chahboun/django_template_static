import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument("template_path")

args = parser.parse_args()
if (args.template_path):
    template = open(args.template_path)
    soup = BeautifulSoup(template.read(), "html.parser")
    for href in soup.select("[href]"):
        item = href.attrs['href']
        is_path = not item.startswith(
            ("http", "www", "#")) and item.find('.') != -1
        if (is_path):
            href.attrs['href'] = "{% static '"+item+"'%}"
            print("Replaced "+item+" to "+href.attrs['href'])
    for src in soup.select("[src]"), :
        for attr in src:
            item = attr.attrs['src']
            is_path = not item.startswith(("http", "www"))
            if (is_path):
                attr.attrs['src'] = "{% static '"+item+"'%}"
                print("Replaced "+item+" to "+attr.attrs['src'])

    soup = "{% load static %}\n"+str(soup)
    template.close()
    open(args.template_path, "w").write(soup)
