import requests
import re
import urllib.request

url = "http://www.apache.org/dist/httpd/"
response = requests.get(url)
html = response.content
print ("Exampe : httpd-2.4.29.tar.gz    Major = 2.4   Minor = 29 ")
major = input("Enter a Major Version : ")
minor = input("Enter a Minor Version : ")
versions_list = []
try:
    versions_list.append(re.findall( r"(httpd-{0}.{1}.tar.bz2)".format(major,minor), str(html))[0])
    versions_list.append(re.findall( r"(httpd-{0}.{1}.tar.gz)".format(major,minor), str(html))[0])
    print (versions_list)
    ext = input("please enter your file extension ( gz or bz2 ) ?")
    matching = [temp for temp in versions_list if ext in temp]
    file_name = matching[0]
    print ('downloading please wait ...')
    urllib.request.urlretrieve(url+file_name, file_name)
    print ("file successfully downloaded")

except IndexError:
    print('Not available required package')
    
    
        
