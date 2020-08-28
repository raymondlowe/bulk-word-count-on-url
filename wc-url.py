import os.path
import argparse
from validators import url as urlvalidator

parser = argparse.ArgumentParser()

parser.add_argument("urlorfile", help="URL to be processed or text file with list of URLs, one per line")

parser.add_argument("-t","--tags",default='body', help="list of tags to include, defaults to body.  example --tags p,h1,h2,li")


args = parser.parse_args()

urlorfile = args.urlorfile

tags = args.tags

if urlvalidator(urlorfile):
    urls = [urlorfile]
else:
    if os.path.isfile(urlorfile):
        with open(urlorfile) as f:
            urls = f.readlines()
        urls = [x.strip() for x in urls] 
    else:
        Exception('Not URL or file')

print(urls)


print("--end--")


