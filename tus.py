import pandas as pd
import tushare as ts
import pymysql
pymysql.install_as_MySQLdb()
import matplotlib as mpl
import matplotlib.pyplot as plt

code_wm = '603066.SH'
start_dt = '20200101'
end_dt = '20200423'

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.xlabel(u'days')  # x轴标签
plt.ylabel(u'value')  # y轴标签
plt.title(u'{}数据'.format(code_wm))  # 图的名称

def stock_daily(code_wm,start_dt,end_dt):
    from sqlalchemy import create_engine
    ce = create_engine('mysql+pymysql://root:coship@localhost:3306/stock?charset=utf8MB4')
    ts.set_token('27d3ec8f12b7f7ec97347be090dc0e4723432263753e10ebd144d996')
    pro = ts.pro_api()
    stock_fields = 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount'
    dat = pro.daily(ts_code=code_wm, start_date=start_dt, end_date=end_dt, fields=stock_fields)
    #print(type(dat))
    data = pd.DataFrame(dat)
    #print(data.describe())
    #data.set_index('trade_date', inplace=True)
    data = data.set_index(data['trade_date']).sort_index()
    data['amount'].plot(label='金额')
    data['vol'].plot(label='总手')
    plt.legend()
    plt.show()
    #dat.to_sql('stock_{}'.format(code_wm).lower(), ce, index=False)
    #print('{}日线行情成功导入数据库'.format(code_wm))


if __name__ == '__main__':
    stock_daily(code_wm, start_dt, end_dt)
