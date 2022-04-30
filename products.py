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

for p in products:
	#print(p)#印出大清單[['拉麵','220'], ['泡麵','35']]
	           	#(p)小清單的名稱價格
	           	#['拉麵', '220']
	           	#['泡麵', '35']
	#print(p[0])#印出大清單[['拉麵','220'], ['泡麵','35']]
	           	#(p)小清單的第0格=name名稱    
	           	#拉麵
	           	#泡麵
	print(p[0], '的價格是', p[1]) #印出大清單[['拉麵','220'], ['泡麵','35']]
	           	#(p)小清單的名稱價格
	           	#拉麵的價格是220
	           	#泡麵的價格是35
