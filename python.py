import requests
from bs4 import BeautifulSoup
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=' + key + '&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.3'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)

print("{0} 기준 {1}의 미세먼지 농도는 {2}입니다.".format(time,location,dust))

dust = 1
if dust > 150:
    print("매우나쁨!! 마스크쓰세요")
elif dust > 80:
    print("나쁨")
elif dust > 30:
    print("보통")
else:
  print("좋음")
  