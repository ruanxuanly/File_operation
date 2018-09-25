from bs4 import BeautifulSoup
import urllib3
pre_url = ''
def get_html_content(url):
    try:
        http = urllib3.PoolManager()
        userAgent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        res = http.request(url=url,method='get',headers={'User_Agent':userAgent})
        return res.data
    except Exception:
        print(Exception)
        return None

def get_soup(url):
    if not url:
        return None
    try:
        soup = BeautifulSoup(get_html_content(url),'lxml')
    except Exception:
        print(Exception)
        return None
    return soup

def main():
    url = read_url()
    if url.find('http') < 0:
        # url = 'http://www.biqugew.com/book/49/2006013.html'
        url = 'http://www.biqugew.com/book/9229/3463155.html'
    while True:
        url = show_content(url)
        # save_url(url)
        str = input()
        if str.__eq__('q'):
            break
        if str.__eq__('p'):
            url = pre_url
            # show_content(pre_url)
        print('\n\n\n\n\n')
def save_file(url):
    next_url = url
    with open('test.txt','w',encoding='utf-8') as fd:
        while True:
            soup = get_soup(next_url)
            try:
                chap = soup.select('.bookname > h1')[0].get_text()
                ele = soup.select('#content')[0].get_text()
            except IndexError:
                print("全部下载完成")
                break
            fd.write(chap+'\r\n')
            next = soup.find_all('a')
            for k in next:
                if k.string is not None:
                    if '下一章'.__eq__(k.string):
                        next_url = 'http://www.biqugew.com' + k['href']
            if ele.__len__() > 0:
                content = ele.replace('<br/>', '\r\n')
                content = content.replace('\xa0\xa0\xa0\xa0', '')
                content = content.replace('笔趣阁', '')
                content = content.replace('www.Biqugew.Com 更新速度最快!', '')

                lines = content.split('\n\r\n')
                fd.writelines(lines)
                fd.write('\r\n')
                print("Download:"+chap+' Done！')
            else:
                print("Download:" + chap + ' False！')

def save_url(url):
    fd = open('E:\PycharmProject\FileOpt\save.cfg','w',encoding='utf-8')
    fd.seek(0)
    fd.write(url)
    fd.close()
def read_url():
    fd = open('E:\PycharmProject\FileOpt\save.cfg', 'r', encoding='utf-8')
    url = fd.readline()
    fd.close()
    return url

def show_content(url):
    global pre_url
    # url = 'http://www.biqugew.com/book/49/2006013.html'
    # http: // www.biqugew.com / book / 49 / 2006011.html

    soup = get_soup(url)
    # ele = soup.find_all('div',id='content')[0]
    ele = soup.select('#content')
    chap = soup.select('.bookname > h1')[0].get_text()
    print(chap)
    next = soup.find_all('a')
    next_url = ''
    for k in next:
        if k.string is not None:
            if '下一章'.__eq__(k.string):
                next_url ='http://www.biqugew.com'+ k['href']
            if '上一章'.__eq__(k.string):
                pre_url ='http://www.biqugew.com'+ k['href']
    if ele.__len__() > 0:
        ele = ele[0]
        # div = soup.div
        content = str(ele).replace('<br/>','')
        content = content.replace('<div id="content">','')
        content = content.replace('\xa0\xa0\xa0\xa0', '')
        content = content[0:content.find('大家搜索')]
        lines = content.split('\n\r\n')
        # print(lines)
        for line in lines[:-1]:
            len = line.__len__()
            if line.__len__() > 50:
                cnt = 1
                while (len - 50*cnt) > 0 :
                    print(line[(cnt-1)*50:cnt*50])
                    cnt += 1
                print(line[50*(cnt-1):])
            else:
                print(line)
    return next_url
if __name__ == '__main__':
    # main()
    save_file('http://www.biqugew.com/book/9229/3463155.html')



