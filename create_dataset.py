import numpy as np
from datetime import datetime
from data_download import BitcoinScraper


# def create_dataset(lookback=24):
#     hurl = "https://production.api.coindesk.com/v2/price/values/BTC"
#     rurl = 'http://www.bitcoinexchangerate.org/'
#     scaper = data_download.BitcoinScraper(hurl, rurl)
#     # scaper.getRealTimeData(True)
#     historicaldata = scaper.getHistoricalData("2019-09-30T08:00", "2019-10-30T08:00", "false")
#     train_dataX, train_dataY = [], []
#     for i in range(len(historicaldata)-lookback-1):
#         train_dataX.append(historicaldata[i:lookback+i,1])
#         train_dataY.append(historicaldata[i+lookback+1,1])
#     train_dataX = np.array(train_dataX)
#     train_dataY = np.array(train_dataY)
#     # print(train_dataX)
#     return train_dataX, train_dataY

def download_data(start_date='2018-05-31T08:00', num_weeks=100):
    date_format = '%Y-%m-%dT%H:%M'
    start = datetime.strptime(start_date, date_format)
    start = start.timestamp()
    dataset = np.array([])
    scraper = BitcoinScraper()

    # repeatedly download data
    for i in range(num_weeks):
        # end_time = start_time + 1 week
        end = start+3600*24*7
        # from timestamp(float) to datetime
        start_time = datetime.fromtimestamp(start)
        end_time = datetime.fromtimestamp(end)
        # datetime to string
        start_time = datetime.strftime(start_time, date_format)
        end_time = datetime.strftime(end_time, date_format)
        # download weekly data
        data = scraper.getHistoricalData(start_time,end_time,'false')
        # print(data.shape)
        dataset = np.append(dataset, data[:,1])
        # set start for the next data
        start = end
    # save dataset to csv
    np.savetxt('dataset.csv', dataset, delimiter=',')



def create_dataset(dataset, lookback=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-lookback-1):
        data = dataset[i:(i+lookback)]
        dataX.append(data)
        dataY.append(dataset[i+lookback])
    return np.array(dataX), np.array(dataY)