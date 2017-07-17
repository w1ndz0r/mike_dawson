import requests
import time

# config
ferma = '1060'
link = 'http://zcash.flypool.org/api/miner_new/t1VHa6sZsxGqD88pjVzaaeprWu21DrMt3ai'


timestamp = int(time.time())
r = requests.get(link)
lastime = r.json().get('workers').get(ferma).get('workerLastSubmitTime')
difference = int(timestamp) - int(lastime)
print(difference)

#lastime_fib = r.json().get('workers').get('fib').get('workerLastSubmitTime')
#lastime_470 = r.json().get('workers').get('470').get('workerLastSubmitTime')
#lastime_default = r.json().get('workers').get('default').get('workerLastSubmitTime')

#print(timestamp)
#if int(timestamp) - int(lastime) > 600:
#    print('pizdarique:', ferma, 'offline')
#else:
#    print('vse norm')

#print('currrent time', timestamp)
#print('1060:', r.json().get('workers').get('1060').get('workerLastSubmitTime'))
#print('fib:', r.json().get('workers').get('fib').get('workerLastSubmitTime'))
#print('470:', r.json().get('workers').get('470').get('workerLastSubmitTime'))
#print('default:', r.json().get('workers').get('default').get('workerLastSubmitTime'))