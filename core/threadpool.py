import threading
import Queue

class ThreadPool(object):



    def __init__(self,thread_num=10):
        self.threads = []
        self.work_queue=Queue.Queue()
        self.thread_num=thread_num


    """
    add a work into work list
    """
    def add_job(self,function,*args):
        self.work_queue.put((function,list(args)))



    def __init_work_queue(self, work_num):
        for i in range(work_num):
            self.add_job(job)

    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work())



class Work(threading.Thread):
    def __init__(self,work_queue):
        threading.Thread.__init__(self)
        self.work_queue=work_queue
        self.start()

    def run(self):
        while True:
            try:
                do, args = self.work_queue.get(block=False)
                do(args)
                self.work_queue.task_done()
            except:
                break