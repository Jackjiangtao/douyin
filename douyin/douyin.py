import requests
import urllib.request

from bs4 import BeautifulSoup as bs
import requests
import sys
import string


#下载文件
def downloadFile(url,mp4Name):

	res = requests.get(url)

	with open(mp4Name, "wb") as code:
		code.write(res.content)
	print("下载完成"+mp4Name)



def get_url(url):
        headers ={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'}
        req = requests.get(url, headers=headers)
        data = req.json()
        data = data['aweme_list']
        for info in  data:
               shareurl =info['aweme_info']['video']['play_addr']['url_list'][0]
               mp4Name =info['aweme_info']['desc']+".mp4"
               downloadFile(shareurl,mp4Name)



if __name__ == "__main__":
    get_url("https://aweme.snssdk.com/aweme/v1/hotsearch/aweme/billboard/")