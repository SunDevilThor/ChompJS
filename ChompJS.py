# ChompJS
# Tutorial from John Watson Rooney YouTube channel

# Documentation for ChompJS: https://github.com/Nykakin/chompjs

# Usage: chompjs can be used in web scrapping for turning JavaScript objects embedded in pages into valid Python dictionaries.
## Think of it as a more powerful json.loads. 

import json
from requests_html import HTMLSession
import chompjs

s = HTMLSession()

url = 'http://quotes.toscrape.com/js/'

r = s.get(url)

#print(r.html.html)

script_css = 'script:contains("var data")'
script_text = r.html.find(script_css, first=True)

json_data = chompjs.parse_js_object(script_text.text)
#print(json_data)

for quote in json_data:
    print(quote['text'])