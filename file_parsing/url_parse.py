import requests
from html_table_parser import HTMLTableParser


#list = ('NEM','Ripple','BitShares','EOS','Waves','Steemit','Golem','Gnosis','Siacoin','ByteCoin','Dogecoin','Augur',
#        'Lisk','Stellar','Byteball','Factom','MaidSafeCoin','Tether','Gamecredits','Decred','Ardor','Status','Komodo','DigixDAO','PIVX','DigiByte','Nxt')
list = ('bytecoin-bcn','steem')


for l in list:
    link = 'http://coinmarketcap.com/currencies/'+str(l)+'/historical-data/?start=20110101&end=20170712'
    filename = str(l)+'.csv'
    f = requests.get(link)
    p = HTMLTableParser()
    p.feed(f.text)
    main_list = p.tables
    print(link)
    print(filename)
    with open(filename, "w") as w:
        for i in main_list:
            for n in reversed(i):
                if n[0] == 'Date' : continue
                if n[0] == '': continue
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