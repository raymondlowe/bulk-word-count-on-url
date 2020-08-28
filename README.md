# bulk-word-count-on-url

Check how many "Words" there are on a url or list of urls.

By default checks the <body>, but can be also used to check <p> or <article> or any other item that may more accurately reflect what the actual content is.

Simplistic definition of word is "string separated by space".

installation:

pip3 install -r requirements.txt

usage:

python3 wc-url.py [url|file-of-urls.txt] [-t|--tag body|p|p,h1,li|<other valid list of elements>]

