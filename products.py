#讀取檔案
def read_file(filename):
	products = []
	with open(filename, "r", encoding="utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name, price = line.strip().split(",")
			products.append([name, price])
	return products

#使用者輸入
def input_product(products):
	while True:
		name = input("請輸入商品名稱(輸入q退出程式):")
		if name == "q":
			break
		price = input("請輸入商品價格:")
		products.append([name, price])
	return products

#印出內容
def print_content(products):
	for p in products:
		print(p[0], "的價格是:", p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename,"w", encoding = "utf-8") as f:
		f.write("商品,價格\n")
		for p in products:
			f.write(p[0] + "," + p[1] + "\n")

def main(filename):
	import os
	products = []
	if os.path.isfile(filename):
		print("開啟舊檔")
		products = read_file(filename)
	else:
		print("找不到檔案, 新增檔案")
	products = input_product(products)
	print_content(products)
	write_file(filename, products)

main("products.csv")