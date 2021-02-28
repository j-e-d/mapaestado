import datetime
import requests

fname = 'estructura_autoridades_apn_{}.csv'
base_url = 'https://mapadelestado.jefatura.gob.ar/seriesdetiempo/dataset/'
first_day = datetime.date.fromisoformat('2016-10-01')
last_day = datetime.date.today()
current_day = first_day
print(first_day, last_day)
while current_day <= last_day:
    current_fname = fname.format(current_day.strftime('%Y%m%d'))
    url = base_url + current_fname
    r = requests.get(url)
    if r.status_code == 200:
        print(current_day)
        open(current_fname, 'wb').write(r.content)
    current_day += datetime.timedelta(days=1)
