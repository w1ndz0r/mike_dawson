from datetime import datetime

wrong = 'Jul 06, 2017'

datetime_object = datetime.strptime(wrong, '%b %d, %Y')
print(datetime_object)