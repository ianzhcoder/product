import os   #operating system
#Refactor 程式重構

#讀取檔案
def read_file(filename):
        products = []
        with open (filename, 'r', encoding = 'utf-8') as f:
            for line in f:
                #刪除欄位名稱 利用continue 跳下一輪
                if '商品,價格,備註' in line:
                    continue
                #strip去除換行符號\n
                #利用spilt中的符號切割
                #p =line.strip().split(',')
                #product =[0]
                #price = [1]
                #可簡化成            
                product, price, detail = line.strip().split(',')
                #存到清單中
                #products.append(p)
                products.append([product,price,detail])
        return products

#使用者輸入
def user_input(products):
    while True:
        product = input ("請輸入商品名稱:")
        if product == 'q' or product == "Q":
            break
        price = int(input ("請輸入" + product + "商品售價:"))
        #新增備註欄位，允許空白
        detail = input ("備註:")
        #p = []
        #p.append(product)
        #p.append(price)
        #可簡化成:
        #p = [product,price]
        #products.append(p)
        #可再簡化成:
        products.append([product,price,detail])
        
    return products    #二維 [[],[]]

#for Loop
#印出購買紀錄
def print_products(products):
    for p in products:
        print (p[0], "的售價是:", p[1], "備註:", p[2])

#存成檔案.txt & .csv
#目錄已存在相同名稱則覆蓋該檔案
def write_file_txt(filename,products):
    with open ('products.txt', 'w') as f:
        for p in products:
            #write 內容為一字串，故只能使用'+'串接str內容
            #當串接內容不是str時，應轉換型別為str
            f.write(p[0] + ',' + str(p[1]) + '\n')
#解決亂碼問題 寫入時加入encoding
def write_file_csv(filename,products):
    with open (filename, 'w', encoding = 'utf-8') as f:
        #加入欄位名稱
        #f.write('商品' + ',' + '價格' + '\n')
        f.write('商品,價格,備註 \n')
        for p in products:
            #判斷備註欄位有沒有資料，沒有則帶入預設值
            if p[2] != '':
                f.write(p[0] + ',' + str(p[1]) + ',' + p[2] + '\n')
            else: 
                f.write(p[0] + ',' + str(p[1]) + ',' + 'no detail' + '\n')


#定義程式進入點 main
def main():
    #檢查檔案是否存在
    filename = 'products.csv'           #減少重複性
    if os.path.isfile(filename):  #此處為相對路徑
        print ("read Success ...")
        products = read_file(filename)
    else:
        print ("找不到該檔案...")

    products = user_input(products)
    print_products(products)
    write_file_csv(filename,products)

#真正執行main
main()