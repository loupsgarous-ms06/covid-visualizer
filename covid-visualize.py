import pandas
import matplotlib
import matplotlib.pyplot

pcr_positive_daily:str = "https://www.mhlw.go.jp/content/pcr_positive_daily.csv"

def getdata(uri):
    try:
        data = pandas.read_csv(pcr_positive_daily)
        data.to_csv('recent_cache_' + uri.rsplit('/',1)[1])
    except:
        data = pandas.read_csv('recent_cache_' + uri.rsplit('/',1)[1])
    return data


def main():
    data = getdata(pcr_positive_daily)
    data['日付'] = pandas.to_datetime(data['日付'])
    data.set_index('日付',inplace = True)
    data['PCR 検査陽性者数(7日間移動平均)'] = data['PCR 検査陽性者数(単日)'].rolling(7).mean()
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
    # print(data)
    matplotlib.pyplot.plot(data)
    matplotlib.view()

if __name__ == "__main__":
    main()