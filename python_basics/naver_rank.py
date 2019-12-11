import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(response, 'html.parser')

#select = soup.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > li:nth-child(1) > span.ah_k ')
#for i in range(1,10):
 #   print(select.text)

tags = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base .ah_k')
for tag in tags:
    print(tag.text)


#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(2) > a > span.ah_k

#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul

with open('naver.txt', 'w', encoding="utf-8") as f:
    f.write('네이버 검색어 순위 \n')
    for i, tag in enumerate(tags):
        f.write(f'{i+1}. {tag.text} \n')
