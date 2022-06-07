from flask import Flask, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import fileinput

app = Flask(__name__)

@app.route('/')
def list():
    url = "https://en.wikipedia.org/wiki/Bond_girl"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html')
    # soup.contents
    Femme_Fatale_href = soup.find('a',href="/wiki/Femme_fatale")
    Bond_Girls_Table=Femme_Fatale_href.find_next('table')
    Bond_Girls_Text_List=Bond_Girls_Table.text
    
    Actress_Count=Bond_Girls_Text_List.count("(")
    Char=0
    End=0
    Actresses_List = []
    
    for Actress in range(Actress_Count):
        Start = Bond_Girls_Text_List.find("(", End)
        Start += 1  # skip the bracket, move to the next character
        End = Bond_Girls_Text_List.find(")", Start)
        Result=Bond_Girls_Text_List[Start:End]
        
        if Actresses_List.count(Result) == 0:
            Actresses_List.append(Result)    
        
    return Actresses_List

@app.route('/healthz')
# Added healthcheck endpoint
def healthz():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
