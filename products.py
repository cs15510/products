"""products = []
while True:
	name = input("請輸入商品名稱: (輸入q結束)")
	if name == 'q':
		break
	price = input("請輸入商品價格:")
	products.append([name, price])

print("輸入的商品有")
for p in products:
	print(p[0], "的價格為:", p[1])

with open("products.csv","w") as f:
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")"""

#讀取檔案
import os
products = []
if os.path.isfile("products.csv"):
	print("開啟舊檔")
	with open("products.csv", "r", encoding="utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
else:
	print("新增檔案")

#使用者輸入
while True:
	name = input("請輸入商品名稱(輸入q退出程式):")
	if name == "q":
		break
	price = input("請輸入商品價格:")
	products.append([name, price])

#印出內容
for p in products:
	print(p[0], "的價格是:", p[1])

#寫入檔案
with open("products.csv","w",encoding = "utf-8") as f:
	f.write("商品,價格\n")
	for p in products:
		f.write(p[0] + "," + p[1] + "\n")