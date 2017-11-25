import requests

def main():
    r = requests.get(
        'URL_Setting')
    print (r.status_code)
    

if __name__=='__main__':
    main()
