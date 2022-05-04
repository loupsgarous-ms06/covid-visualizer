import matplotlib
import matplotlib.pyplot
import mhlwcovidparser

def main():
    mcp = mhlwcovidparser.mhlwCovidParser()
    data = mcp.prefecture(["ALL","Tokyo"])

    # data = getdata(pcr_positive_daily)
    # data['PCR 検査陽性者数(7日間移動平均)'] = data['PCR 検査陽性者数(単日)'].rolling(7).mean()
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
    # print(data)
    matplotlib.pyplot.plot(data)
    matplotlib.pyplot.show()

if __name__ == "__main__":
    main()