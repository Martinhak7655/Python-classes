import requests

# try:
#     item_id = input("Greq tan aydin ev kstanaq admini idn")

#     res = requests.get(f"https://service.homely.am/api/item/get?itemId={item_id}")
#     if res.status_code == 200:
#        data = res.json()["data"]
#        print(data[0]["adminid"])
#     elif res.status_code == 404:
#         print("Api not found") 
# except:
#     print("Error")

# try:
#     country_name = input("Enter Country Name:  ")
    
#     res = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
#     data = res.json()
#     print(f"Population: {data[0]["population"]}")
# except:
#     print("Error")

# try:
#     country_capital = input("Enter Country Name:  ")

#     res = requests.get(f"https://restcountries.com/v3.1/name/{country_capital}")
#     data = res.json()
#     print(f"Capital City: {data[0]["capital"][0]}")
# except:
#     print("Error")

#bot harcnuma inch vor erkri anun harcneluc heto inqy uxarkuma mayraqaxaqi anuny ev bnakcutyan tivy