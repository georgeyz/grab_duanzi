#encoding:utf-8
import re
import requests
from bs4 import BeautifulSoup

def gethtml(url):
        content=requests.get(url)
        content.encoding="utf-8"
        html=content.text
        return html
def getduanzi(num):
    soup_duanzi=[]
    for n in range(1, int(num)+1):
        url=url_base+str(n)
        html=gethtml(url)
        soup=BeautifulSoup(html,'lxml')
        soup_duanzis=soup.select('div[class="j-r-list-c-desc"] a')
        for i in range(len(soup_duanzis)):
            r=re.compile(r'^<a.*?>\s+([\s\S]*)</a>$')
            strl=str(soup_duanzis[i])
            if '<br/>' in strl:
                strll=re.sub(r'<br/>', '\n', strl)
            else:
                strll=strl
            duanzi=re.findall(r,strll)
            soup_duanzi.append(duanzi)
    return soup_duanzi 
def save_duanzi(listl):
    with open('duanzi1.txt','w',encoding='utf-8') as f:
        for m in listl:
            listll='%s'*len(m)% tuple(m)

            f.write(listll+'\n'+'\n')
            
        
if __name__=='__main__':
    url_base='http://www.budejie.com/text/'
    num=input('请输入要抓取段子的页数：')
    soup_duanzi=getduanzi(num)
    save_duanzi(soup_duanzi)
    print('总共抓取了%s页段子'%num)
