'''东方财富网股票数据'''
from selenium import webdriver
from time import sleep
import sqlite3
from selenium.common.exceptions import NoSuchElementException
import xlwt

if __name__ == '__main__':
    main()

def main():
    url = 'http://quote.eastmoney.com/center/boardlist.html#boards-BK04471'
    saveconnect = sqlite3.connect("general-design.db")
   # init_DataBase(saveconnect)
    # file = open("东方财富股票数据.xls",'w',encoding="utf-8")
    savepath = "东方财富股票数据.xls"
    driver = webdriver.Chrome(r"chromedriver.exe")# D:\大三课程资料\Python\python实验\
    datalist = getStockData(driver,url)
    saveData2excel(datalist, savepath)
    saveData2DataBase(datalist, saveconnect)

def extractor(driver,xpath_text):
    '''根据xpath获取内容'''
    TCases = driver.find_element_by_xpath(xpath_text)
    return TCases.text

def init_DataBase(saveconnect):
    cur = saveconnect.cursor()
    sql = '''
        create table 东方财富网股票代码
        (id integer primary key autoincrement not null,
        code text not null,
        sname text not null,
        newprice  text not null,
        updownscpoe text not null,
        updownprice text not null,
        submitquan text not null,
        submitprice text not null,
        zhenfu text not null,
        maxprice text not null,
        minprice text not null,
        todayopen not null,
        yestergain not null,
        quancmp text not null,
        change text not null,
        raise text not null,
        pureraise text not null
        );
        '''

    cur.execute(sql)  # 执行操作请求
    saveconnect.commit()  # 对象提交数据库的操作
    print("创建数据库表成功~")

    cur.execute('insert into 东方财富网股票代码 values(0,"代码","名称","最新价","涨跌幅","涨跌额","成交量","成交额","振幅","最高价","最低价","今开","昨收","量比","换手率","市盈率","市净率")' )
    saveconnect.commit()  # 对象提交数据库的操作
    saveconnect.close()

def saveData2excel(datalist,savepath):
    print("Loading to Save......")
    column = ('代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量', '成交额', '振幅', '最高价', '最低价', '今开',
              '昨收', '量比', '换手率', '市盈率', '市净率')
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # xlwt.Workbool(解码标准)  创建excel对象
    sheet = book.add_sheet("东方财富网股票",cell_overwrite_ok=True)  # 创建一个单元sheet1
    for i in range(0,len(column)):
        sheet.write(0,i,column[i])
    for j in range(0,112):
        print("写入到第%d条"%(j+1))
        data = datalist[j]
        for k in range(0,len(column)):
            sheet.write(j+1,k,data[k])
    book.save(savepath)
    print("获取完毕~")

def saveData2DataBase(datalist,saveconnect):
    print("已成功连接到数据库~")
    c = saveconnect.cursor()

    for j in range(0,112):
        print("-----------")
        data = datalist[j]

        c.execute(  'insert into 东方财富网股票代码(id,code,sname,newprice,updownscpoe,updownprice,submitquan,submitprice,zhenfu,maxprice,minprice,'
                    'todayopen,yestergain,quancmp,change,raise,pureraise'')'
                    'values("%d","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
                    %(j+1, data[0], data[1], data[2], data[3], data[4],data[5],data[6], data[7], data[8],
                      data[9],data[10],data[11], data[12], data[13], data[14],data[15])  )
        saveconnect.commit()  # 提交数据库的操作
        print("爬取到第%d条"%(j+1))

    saveconnect.close() # 关闭数据库

def getStockData(driver,url):
    datalist = []
    driver.get(url)
    sleep(3)
    for page_num in range(1, 6 + 1):
        for i in range(1, 10 + 1):
            # print(i + (page_num - 1) * 20)
            for ele_type in ['odd', 'even']:
                stock_dict = {}
                number_list = ['2', '3', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
                ele_list = ['代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量', '成交额', '振幅', '最高价', '最低价', '今开',
                            '昨收', '量比', '换手率', '市盈率', '市净率']
                for j, name in zip(number_list, ele_list):
                    try:
                        temp_xpath = "/html/body/div[@class='page-wrapper']/div[@id='page-body']/div[@id='body-main']/div" \
                                     "[@id='table_wrapper']/table[@id='table_wrapper-table']/tbody/tr[@class='{}'][{}]/td[{}]".format(
                            ele_type, i,j)
                        stock_dict[name] = extractor(driver,temp_xpath)
                    except NoSuchElementException as e:
                        if hasattr(e, "reason"):
                            print(e.reason)
                            break
                datalist.append(list(stock_dict.values()))
        # 下一页
        try:
            driver.find_element_by_xpath(
                "/html/body/div[@class='page-wrapper']/div[@id='page-body']/div[@id='body-main']/div[@id='table_wrapper']/div"
                "[@class='dataTables_wrapper']/div[@id='main-table_paginate']/a[@class='next paginate_button']").click()
        except NoSuchElementException as e:
            if hasattr(e, "reason"):
                print(e.reason)
            break
        sleep(1)
    driver.close()
    # print(datalist)
    return datalist




