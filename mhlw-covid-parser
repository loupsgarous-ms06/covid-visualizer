import pandas
import matplotlib
import matplotlib.pyplot

# import enum

class mhlwCovidParser:
    def __init__(self):
        uri:str = "https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv"
        try:
            dl_data = pandas.read_csv(uri)
            dl_data['Date'] = pandas.to_datetime(dl_data['Date'])
            dl_data.set_index("Date", inplace = True)
            dl_data.to_csv('recent_cache_' + uri.rsplit('/',1)[1])
            self.data = dl_data.copy()
        except:
            print("Currently, I cannot access the required resources. Therefore, we utilize the most recently cached data. We apologize for any inconvenience.")
            self.data = pandas.read_csv('recent_cache_' + uri.rsplit('/',1)[1])
        self.pref_enum_list = self.data.columns.tolist()

    def daily(self, date):
        daily_data = self.data.set_index("Date")
        # print(type(daily_data.index[3]))
        # if type(date) != timestamp
        date = pandas.to_datetime(date)
        # print(type(date))
        return_data = daily_data[daily_data.index == date]
        return return_data

    def prefecture(self, pref):
        # if pref in self.pref_enum_list:
        return self.data[[pref]]

if __name__ == "__main__":
    mcp = mhlwCovidParser()
    # data = mcp.daily("2021/08/31")
    # print(mcp.data)
    print(mcp.prefecture("UNKO"))


