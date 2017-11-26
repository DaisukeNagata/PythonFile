import requests
import time
from datetime import datetime
# -*- coding: utf-8 -*-
import sys
import io

def main():
    #cron対応
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
  
    start = time.time()
   
    r = requests.get('URLSettings')
    t = time.time()

    
    elapsed_time =  time.time() - start
    text = datetime.now().strftime("%Y/%m/%d %H:%M:%S")+" "+"StatusCode"+str(r.status_code)+" "+"経過時間"+str(elapsed_time)

    print(text)


if __name__=='__main__':
    main()
