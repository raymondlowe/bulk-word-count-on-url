# bulk-word-count-on-url

Check how many "Words" there are on a url or list of urls.

By default checks the body gag, but can be also used to check p or article or any other item that may more accurately reflect what the actual content is.

Word separation done using regex search so handles spaces and punctuation.

## installation:

```
git clone https://github.com/raymondlowe/bulk-word-count-on-url.git
cd bulk-word-count-on-url
pip3 install -r requirements.txt
```

## usage:

```
python3 wc-url.py [url|file-of-urls.txt] [-t|--tag body|p|p,h1,li|<other valid list of elements>]
```

## Example:

```
python3 wc-url.py example.txt --tags p 
```

Outputs:

```
"http://example.com", 26
"https://www.example.com", 26
--end--
```

Because there are 26 words within the paragraphs of the page.


## Note:

Includes caching, delete the file wc-url-cache.sqlite to clear the cache.

## Troubleshoot ssl errors

```
pip3 install --upgrade certifi
pip3 install --upgrade urllib3[secure]
pip3 install --upgrade requests
export PYTHONWARNINGS="ignore:Unverified HTTPS request".
```

### Caution:

It will double count if you choose tags that may be inside one another. e.g. --tags body,p

