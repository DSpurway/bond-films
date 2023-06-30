from flask import Flask, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

app = Flask(__name__)

@app.route('/')
def list():
    url = "https://www.pocket-lint.com/tv/news/148096-james-bond-007-best-movie-viewing-order-chronological-release"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html')
    # soup.contents

    Bond_Film_Quick_List = soup.find("p", string="This is the same list as above, only spoiler-free and much quicker to read:")
    Bond_Film_Date_List=Bond_Film_Quick_List.find_next("ul").text
# Bond_Film_Date_List=Bond_Film_Quick_List.next_sibling.text
    return Bond_Film_Date_List

@app.route('/healthz')
# Added healthcheck endpoint
def healthz():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
