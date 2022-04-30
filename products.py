# products = []
# while True:
#     name = input('請輸入商品名稱:')
#     if name == 'q':
#     	break
#     products.append(name)	
# print(products)    #只問商品名稱 可無限輸入

products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q': 
    	break
    price = input('請輸入商品價格:')	#price價格
    # p = []
    # p.append(name)
    # p.append(price)

    # p = [name, price] #快寫|15~17
    # products.append(p)	
    
    products.append([name, price]) #快寫15~17/19.20
print(products)    
# products[0][0]