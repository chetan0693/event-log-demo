#!/usr/bin/python
# 
# Generate log files
# Log will be of the format :
# date : (SUCCESS|ERROR) : COUNTRY : IP
#

from random import randrange

def random_country():
  countries = ["CN","US","BR","BD","RU","MX","VN","DE","TR","CD","FR","IT","ZA","ES","CO","AR","PL","DZ","UG","PE","AF","MY","VE","GH","KP","SY","RO","LK","CI","CL","BF","MW","EC","ML","ZM","SN","CU","GR","PT","TD","BE","SO","HU","DO","HT","SE","SS","HN","TJ","RS","HK","LY","PY","PG","NI","KG","SK","FI","AE","CF","GE","BA","HR","NZ","PR","LR","UY","MR","CG","AM","JM","LV","MK","SI","XK","GW","SZ","EE","TL","GQ","QA","KM","DJ","BT","SB","LU","MO","MQ","MV","BZ","BS","EH","VU","GF","ST","GU","CW","TO","GD","VC","JE","AG","IM","AW","BM","AS","MP","FO","SX","LI","SM","AX","CK","PW","WF","TV","MS","SH","IO","SJ","NF","TK","CC","PN","IN","ID","PK","NG","JP","PH","ET","EG","IR","TH","GB","MM","KR","UA","TZ","KE","SD","CA","MA","IQ","NP","UZ","SA","YE","TW","MZ","AU","MG","CM","NL","NE","KZ","KH","GT","AO","ZW","RW","CS","TN","CZ","GN","BO","BI","BY","BJ","AZ","AT","CH","IL","BG","TG","JO","LA","SV","ER","DK","SL","NO","TM","SG","IE","CR","MD","LB","PS","LT","PA","MN","AL","OM","KW","NA","BW","LS","GM","GA","MU","TT","CY","FJ","RE","GY","BH","ME","CV","SR","GP","MT","BN","IS","BB","PF","NC","WS","LC","YT","AN","VI","FM","KI","SC","AD","DM","MH","GG","GL","KN","KY","MF","MC","GI","VG","TC","BQ","AI","NR","BL","PM","FK","NU","CX","VA","TF","GS"]
  return countries[randrange(1,248)]

def random_ip():
  not_valid = [10,127,169,172,192]

  first = randrange(1,256)
  while first in not_valid:
    first = randrange(1,256)

  ip = ".".join([str(first),str(randrange(1,256)),
  str(randrange(1,256)),str(randrange(1,256))])
  return ip

def main():
  country = random_country()
  ip = random_ip()

if __name__ == "__main__":
  main()
