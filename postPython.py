import requests

def main():
    r = requests.get(
        'URL_Setting')
    print (r.status_code)
    f = open('text.txt', 'w')
    f.write(str(r.status_code))
    f.close()

if __name__=='__main__':
    main()
