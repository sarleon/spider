#coding:utf-8
from optparse import OptionParser
from optparse import OptionGroup


def banner():
    print "******************************"
    print "Spider v1.0 Powered By Sarleon"
    print "******************************"




def commandLineArgument():
    help_infomation=\
    u"""
     -u 指定爬虫开始地址

    -d 指定爬虫深度

    --thread 指定线程池大小，多线程爬取页面，可选参数，默认10

    --dbfile 存放结果数据到指定的数据库（sqlite）文件中

    --key 页面内的关键词，获取满足该关键词的网页，可选参数，默认为所有页面

    -l 日志记录文件记录详细程度，数字越大记录越详细，可选参数，默认spider.log

    --testself 程序自测，可选参数
    """
    usage=""
    parser=OptionParser()
    # parser.add_option('-h','--help',action='store_true')
    parser.add_option('-u','--url',dest='url',action='store',help=u'爬虫的目标地址')
    (options, args) = parser.parse_args()