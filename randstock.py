from urllib.request import Request, urlopen
from random import randint
from os import remove

stocks = list()
def request():
    url = 'https://www.marketindex.com.au/asx-listed-companies'
    response = urlopen(Request(url, headers={'User-Agent' : 'Mozilla/5.0'}))
    f = open('source.txt', 'wb')
    f.write(bytes(response.read()))
    f.close()
    return open('source.txt', 'r', errors='ignore')

def main():
    f = request()
    skip_head = False

    for line in f:
        if 'Companies might remain on the list' in line:
            skip_head = True

        if skip_head == True and ';path&' in line:
            search(line)
            break
    f.close()
    print(stocks[randint(0, len(stocks))], 'Number of stocks listed on the ASX:', len(stocks))
    f = open('source.txt', 'w')
    for i in stocks:
        f.write(i + '\n')
    f.close()
    

def search(line):
    while ';code&' in line:
        code = line.find(';code&')
        end = line[code + 18:].find('&')
        stocks.append(line[code + 18:code + 18 + end])
        line = line[code + 5:]

main()
