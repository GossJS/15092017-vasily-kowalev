#coding: utf8

import re

data = []
platforms = ['Android', 'iPhone', 'iPad', 'Mac OS', 'Windows', 'Linux']
dictionary = {'platforms': {platform: 0 for platform in platforms}, 'ips': {}}

with open("visits.txt") as file:
    for line in file:
        data.append(line)

for string in data:
    # Извлечение IP.
    ip = string[:15]

    if ip not in dictionary['ips'].keys():
        dictionary['ips'][ip] = 1
    else:
        dictionary['ips'][ip] += 1

    # Извлечение платформы.
    for platform in platforms:
        if re.search(r'' + platform + '', re.findall(r'\(([^)].*?)\)', string)[0]):
            dictionary['platforms'][platform] += 1
            break  # Чтобы Linux/Android и Mac OS/iPhone/iPad считались раздельно.

ips_sorted = sorted(dictionary['ips'].items(), key=lambda item: dictionary['ips'][item[0]], reverse=True)

# Вывод результатов.
for ip_sorted in ips_sorted[:5]:
    print(ip_sorted[0], ip_sorted[-1])

print('---------------')

for platform in platforms:
    print(platform, dictionary['platforms'][platform])