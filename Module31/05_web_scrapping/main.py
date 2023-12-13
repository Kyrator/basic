# TODO здесь писать код
from re import findall



# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
    result_beta = findall(r'>.+</h3>', text)
    release = list(map(lambda x: x[1:-5], result_beta))
    print(release)


