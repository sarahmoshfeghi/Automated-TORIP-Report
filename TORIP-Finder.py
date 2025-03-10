import requests
import re
import pymongo
from mail_send import send_mail


def ip_block():
    resource = ['https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt',
                'https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt'
        , 'https://www.dan.me.uk/torlist/?full']
    ip_block_list = []
    file = open('/pathtothefile/ip-block.csv', 'w')
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient['IPBlockRecommended']
    mycol = mydb['IPBlockRecommended']
    for url in resource:
        source = re.search('http[s]?://(.*?)/', url).group(1)
        r = requests.get(url)
        result = re.findall(r"^\d.*", r.text, re.MULTILINE)
        if result:
            for ip in result:
                if ':' in ip:
                    continue
                # print(ip)
                ip_j = {}
                ip_j['source'] = source
                ip = ip.strip()
                if mycol.count_documents({'ip': ip}, limit=1) != 0:
                    continue
                ip_j['ip'] = ip
                mycol.insert_one(ip_j)
                print(ip)
                file.write(ip + '\n')
    file.close()

    send_mail("test@test.com", "test2@test.com",
              "TOR-IP-Block")


ip_block()
