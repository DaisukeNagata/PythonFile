import requests
from datetime import datetime
def main():
    r = requests.get(
        'URLSetting')
    print (r.status_code)
   
    text = datetime.now().strftime("%Y/%m/%d %H:%M:%S")+"StatusCode"+str(r.status_code)
    
    f = open('text.txt', 'a')
    f.write(text + '\n')
    f.close()

if __name__=='__main__':
    main()
