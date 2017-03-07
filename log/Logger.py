
class Logger:

    log_levels=["FATAL","ERROR","WARNING","DEBUG","INFO"]
    def __init__(self,log_level,log_fileoath="spider.log"):
        self.log_level=log_level or 0
        self.log_filepath=log_fileoath
        self.log_file=open(log_fileoath,'w')


    def log(self,level,infomation):
        infomation_prefix="[%s]" % self.log_levels[level]
        infomation=infomation_prefix+infomation
        if(level<=self.log_level):

            self.log_file.write()


