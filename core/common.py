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
    parser.add_option('-d','--deep',dest='deep',action='store',help=u'爬虫递归的深度',default=10)
    parser.add_option('-t','--thread',dest='threads',action='store',help=u'爬虫的线程数',default=10)
    parser.add_option('--dbfile',dest='dbfile',action='store',help=u'获取结果的存储位置（sqlite数据库）')
    parser.add_option('-k','--key',dest='key',action='store',help=u'页面的关键词，只提取含有关键词的页面，若没有则默认提取所有页面')
    parser.add_option('-l','--log',dest='log',action='store',help=u'日志的记录级别, 0为fatal,1为error,2为warning,3为debug,4为info' ,default=0)
    (options, args) = parser.parse_args()
