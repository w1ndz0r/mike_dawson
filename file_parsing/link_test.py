list = ('NEM','Ripple','BitShares','EOS','Waves','Steemit','Golem','Gnosis','Siacoin','ByteCoin',
        'Dogecoin','Augur','Lisk','Stellar','Byteball','Factom','MaidSafeCoin','Tether','Gamecredits',
        'Decred','Ardor','Status','Komodo','DigixDAO','PIVX','DigiByte','Nxt')

for i in list:
    link = 'http://coinmarketcap.com/currencies/'+str(i)+'/historical-data/?start=20170701&end=20170712'
    print(link)