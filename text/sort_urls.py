import os
language = 'malayalam'
url = 'https://raw.githubusercontent.com/Examination-assist/data_feb23/main/'

# os.system(f"ls | grep \"{language}\\.htm\" | sort -t. -k4,4n > {language}.txt")

with open(f'{language}.txt','r') as f:
    data = f.readlines()
    # print(data)

data = [i.strip() for i in data]
data = sorted(data, key=lambda a: int(a.split(f'.doc {language}.htm')[0][3:]))
urls = urls = [url+"%20".join(i.split(' ')) for i in data]

with open(f'{language} urls.txt', 'w') as f:
    f.write("\n".join(urls))
