
def QA_SU_crawl_eastmoney(action="zjlx", stockCode=None):
    '''

    :param action: zjlx 后期支持其他的操作类型
    :param stockCode: 股票代码
    :return:
    '''
    stockItems = QA_fetch_stock_list()

    if stockCode == "all":
        # 读取tushare股票列表代码
        print("💪 一共需要获取 %d 个股票的 资金流向 , 需要大概 %d 小时" %
              (len(stockItems), (len(stockItems)*5)/60/60))

        code_list = []
        for stock in stockItems:
            code_list.append(stock['code'])
            # print(stock['code'])
        crawl_eastmoney_file.QA_read_eastmoney_zjlx_web_page_to_sqllite(
            code_list)
        # print(stock)

        return
    else:
        # todo 检查股票代码是否合法
        # return crawl_eastmoney_file.QA_read_eastmoney_zjlx_web_page_to_sqllite(stockCode=stockCode)
        code_list = []
        code_list.append(stockCode)
        return crawl_eastmoney_file.QA_request_eastmoney_zjlx(param_stock_code_list=code_list)



def QA_SU_save_financialfiles():
    return save_financialfiles.QA_SU_save_financial_files()


def QA_SU_save_report_calendar_day():
    return save_financial_calendar.QA_SU_save_report_calendar_day()


def QA_SU_save_report_calendar_his():
    return save_financial_calendar.QA_SU_save_report_calendar_his()


def QA_SU_save_stock_divyield_day():
    return save_stock_divyield.QA_SU_save_stock_divyield_day()


def QA_SU_save_stock_divyield_his():
    return save_stock_divyield.QA_SU_save_stock_divyield_his()
