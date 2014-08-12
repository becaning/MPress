# /usr/bin/env python
# -*- coding:utf8 -*-

__author__ = 'becaning'

import markdown
import os
import jinja2
import yaml
import sys
import re

reload(sys)
sys.setdefaultencoding("utf-8")


class Page(object):
    """
    Base Page
    """
    def __init__(self):
        self.conf    = self.getconf()
        self.tplenv  = self.gettplenv()
        self.content = {}
        self.content['index_url'] = 'http://baidu.com/'

    #读取配置文件
    def getconf(self):
        fd = open('conf/conf.yaml')
        return yaml.load(fd)

    #设置jinja2的Environment
    def gettplenv(self):
        return jinja2.Environment(loader=jinja2.FileSystemLoader('themes/default'))

    #Markdown文档转为html
    def md2html(self,md):
        fd = open(md,'r')
        text = fd.read()
        return markdown.markdown(text)

    #渲染模板
    def render_tpl(self,content,template):
        tpl = self.tplenv.get_template(template)
        return tpl.render(content)

    #write something to a html file,
    def writehtml(self,content,path):
        try:
            fd = open(path,'w')
            fd.write(content)
            fd.close()
            return True
        except Exception, e:
            print 'Open file error',e

    #Get file raw name
    def getRawname(self,name):
        if not os.path.isdir(name):
            l = name.split('.')
            l.pop()
            return ''.join(l)

    #Get file extends name
    def getExtname(self,name):
        if not os.path.isdir(name):
            l = name.split('.')
            return l.pop()


class IndexPage(Page):
    '''
    return Index Page
    '''
    def __init__(self):
        super(IndexPage,self).__init__()

    #Generate index.html
    def genIndex(self):
        posts = os.listdir('./post/')
        posts.sort()
        posts.reverse()
        postlist = []

        for name in posts:
            temp = {}
            rawname = self.getRawname(name)
            temp['name'] = rawname
            temp['url'] = rawname+'.html'
            postlist.append(temp)

        self.content['postlist'] = postlist

        html = self.render_tpl(self.content,'index.html')
        self.writehtml(html,'blog/index.html')


class PostPage(Page):
    '''
    return a post
    '''
    def __init__(self):
        super(PostPage,self).__init__()

    #Generate a post
    def genPost(self,md):
        rawname = self.getRawname(md)
        mdhtml = self.md2html('./post/'+md)
        self.content['post'] = mdhtml
        html = self.render_tpl(self.content,'post.html')
        self.writehtml(html,'blog/'+rawname+'.html')

    #Generate all posts
    def genAllposts(self):
        mdlist = os.listdir('./post/')

        for md in mdlist:
            self.genPost(md)


class Tag(Page):
    '''
    return a Tags Page
    '''
    def __init__(self):
        pass



# if __name__ == '__main__':
#     mm = IndexPage()
#     mm.genIndex()
#     p = PostPage()
#     p.genAllposts()






