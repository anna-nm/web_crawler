import os 

def create_project_dir(directory):
  if not os.path.exists(directory):
    print ("Creating project " + directory)
    os.makedirs(directory)

def create_data_files(project_name, base_url):
  queue = project_name + '/queue.txt'
  crawled = project_name + '/crawled.txt'
  if not os.path.isfile(queue):
    write_file(queue, base_url)
  if not os.path.isfile(crawled):
    write_file(crawled, '')

def write_file(path, data):
  os.makedirs(os.path.dirname(path),exist_ok=True)
  with open(path, 'w') as f:
    f.write(data)
    f.close()

# Add data onto an existing file
def append_to_file(path, data):
  with open(path,'a') as file:
    file.write(data + '\n')

# Delete the contents of a file
def delete_file_contents(path):
  with open(path, 'w'):
    pass

# Convert file to set
def file_to_set(file_name):
  result = set()
  with open (file_name, 'rt') as f:
    for line in f: 
      result.add(line.replace('\n','')) #delete extra lines (in line 25)
  return result

# Each item in set is a new line in the file
def set_to_file(links, file):
  delete_file_contents(file)
  for link in sorted(links):
    append_to_file(file, link)
    


