import requests
url='http://127.0.0.1:8000/items/'
name=input('product name: ')
try:
    price=float(input('product price: '))
except:
    print('price value does not match with float data type')
tax_presence=input('insert 1 to add tax or 0 to skip: ')
tax_value=0.0
if tax_presence=='1':
    tax_value=float(input('insert tax value: '))
data={
    'name':name,
    'price':price,
    'tax':tax_value
}
re=requests.post(url, json=data)
print(re.text)