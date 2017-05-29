import time

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger:

    __metaclass__ = 'Singleton'

    log_levels=["FATAL","ERROR","WARNING","DEBUG","INFO"]

    def __repr__(self):
         return "[Logger]"

    def __init__(self,log_level,log_fileoath="spider.log"):
        self.log_level=log_level or 0
        self.log_filepath=log_fileoath
        self.log_file=open(log_fileoath,'w')


    def log(self,level,infomation):
        infomation_prefix="[%s]" % self.log_levels[level]
        if level<=self.log_level:
            current_time=time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())
            self.log_file.write(infomation_prefix+current_time+infomation)




