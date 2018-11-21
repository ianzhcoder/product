products = []
while True:
    product = input ("請輸入商品名稱:")
    if product == 'q' or product == "Q":
        break
    price = input ("請輸入" + product + "商品售價:")
    #p = []
    #p.append(product)
    #p.append(price)
    #可簡化成:
    #p = [product,price]
    #products.append(p)
    #可再簡化成:
    products.append([product,price])
    
print (products)    #二維 [[],[]]
#for Loop
for p in products:
    print (p[0], "的售價是:", p[1])


#存成檔案.txt & .csv
#目錄已存在相同名稱則覆蓋該檔案
with open ('products.txt', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

with open ('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')

