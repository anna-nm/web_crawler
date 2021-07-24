import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

Project_Name = 'tiki'
Homepage = 'https://tiki.vn/'
Domain_Name = get_domain_name(Homepage)
Queue_File = Project_Name + '/queue.txt'
Crawled_File = Project_Name + '/crawled.txt'
Number_Of_Threads = 8
queue = Queue()
Spider (Project_Name, Homepage, Domain_Name)

def create_workers():
  for n in range(Number_Of_Threads):
    t = threading.Thread(target = work)
    t.daemon = True
    t.start()

def work(): 
  while True: 
    url = queue.get()
    Spider.crawl_page(threading.current_thread().name, url)
    queue.task_done()

def create_jobs():
  for link in file_to_set(Queue_File):
    queue.put(link)
  queue.join()
  crawl()

def crawl():
  queued_links = file_to_set(Queue_File)
  if len(queued_links) > 0: 
    print(str(len(queued_links)) + ' links in the queue')
    create_jobs()

create_workers()
crawl()
