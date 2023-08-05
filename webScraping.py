import requests
from bs4 import BeautifulSoup
from routers.config import connection,cursor


url = "https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx"

try:
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 Safari/537.3"}
    response = requests.get(url,headers=headers)
    print("response",response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        data = []
        i = 0
        dim1 = 0
        for tag in soup.find_all('td'):
            # print('data', tag, dir(tag))
            temp = []
            for i in tag.children:
                temp.append(i)
            data.append(temp)
            # print(tag.get('td'))
            # if dim1 < 7:
            #     data[i].append(tag.text)
            #     dim1 +=1
            # else:
            #     data.append([])
            #     dim1 = 0
            #     i+=1
        
            
        print(data)

    else:
        print(f"Request failed with status code: {response.status_code}")

except Exception as e:
    print(f"Error occurred: {e}")
