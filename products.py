products = []
while True:
	name = input("請輸入商品名稱: (輸入q結束)")
	if name == 'q':
		break
	price = input("請輸入商品價格:")
	products.append([name, price])

print("輸入的商品有")
for p in products:
	print(p[0], "的價格為:", p[1])