#coding:utf-8
import requests
import re
class Scraber:

    default_headers={

    }

    url_list=[]
    def __init__(self,url,regex=None,max_depth=10,cookies=None,headers=None):
        self.current_url_index=0
        self.max_depth=max_depth
        self.start_url=url
        self.regex=regex
        self.cookies=cookies
        self.headers=headers

        self.url_list.append(self.start_url)



    def controller(self):
        pass



    def get_page(self,url,current_depth):

        page=requests.get(url,cookies=self.cookies,headers=self.headers)

        #如果不是页面而是其他资源则返回

        if 'text/html' not in page.headers['Content-Type']:
            return False

        if not self.regex:
            pass
        else:
            pattern=re.compile(self.regex)
            match=re.search(pattern,page.text)
            if not match:
                return False



        #从页面中找新的链接
        link_regex=re.compile('<a href="(.*)">.*</a>')
        links=re.findall(link_regex,page.text)
        self.url_list.append(links)
        return page.text