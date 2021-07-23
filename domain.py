#purpose: keep the spiders crawl the domain page only
from urllib.parse import urlparse


# get the domain name - ex: example.com
def get_domain_name(url):
  try: 
    results = get_sub_domain_name(url).split('.')
    return results[-2] + '.' + results [-1]
  except:  
    return 'error'
  


#get sub domain name - ex: name.example.com
def get_sub_domain_name(url):
  try:
        return urlparse(url).netloc 
         #network location
  except:
        return 'error'
  
