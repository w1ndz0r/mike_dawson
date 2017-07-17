import requests
import sys
from html_table_parser import HTMLTableParser

link = sys.argv[1] #link = "http://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20170706"
curr = link.split('/')
filename = str(curr[4]) +'.csv'

f = requests.get(link)

p = HTMLTableParser()
p.feed(f.text)
main_list = p.tables


with open(filename, "w") as w:
    for i in main_list:
        for n in reversed(i):
            if n[0] == 'Date' : continue
            date = n[0].split(' ')
            s = date[1]
            day = s[:-1]
            if date[0] == 'Jan': month = '01'
            if date[0] == 'Feb': month = '02'
            if date[0] == 'Mar': month = '03'
            if date[0] == 'Apr': month = '04'
            if date[0] == 'May': month = '05'
            if date[0] == 'Jun': month = '06'
            if date[0] == 'Jul': month = '07'
            if date[0] == 'Aug': month = '08'
            if date[0] == 'Sep': month = '09'
            if date[0] == 'Oct': month = '10'
            if date[0] == 'Nov': month = '11'
            if date[0] == 'Dec': month = '12'
            year = date[2]
            fulldate = year + '.' + month + '.' + day + ' 00:00'
            n[0] = fulldate
            n[0] = fulldate
            if n[5] == '-':
                n[5] = '0' + "\n"
            else:
                n[5] = n[5].replace(",", "") + "\n"
            line = n[0:6]
            line = ','.join(line)
            w.writelines(line)
w.close()
print('Done. File =', filename)