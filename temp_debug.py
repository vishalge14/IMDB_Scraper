import requests
r = requests.get('https://www.imdb.com/chart/top/', headers={'User-Agent':'Mozilla/5.0'})
print(r.status_code)
idx = r.text.find('<tbody class="lister-list"')
print(idx)
print(r.text[idx:idx+500])
