import pandas as pd
import sys


from market_profile import MarketProfileSlice
from orderflow_plotter import OrderflowPlotter

'''
Plotting of orderflow chart
- Candlestick
- Orderflow data by price level
- Volume bar
- Classic MACD
- CVD
- StochRSI
'''

stock = sys.argv[1]

if __name__ == '__main__':
	inst = 'btcusdt'
	increment = 500
	token = inst.upper()
	interval = '1D'

	# ohlcv = pd.read_csv('examples/data/sample_data_2.csv', index_col=0)
	ohlcv = pd.read_csv(f"./data/price_and_delta/{stock.upper()}-pd.csv", index_col=0)
	ohlcv.index = pd.to_datetime(ohlcv.index)

	profile = pd.read_csv(f"./data/stack_orderflow/{stock.upper()}-orderflow.csv")
	# profile = pd.read_csv('examples/data/orderflow_data.csv')
	profile['t'] = pd.to_datetime(profile['t'])

	mp_slices=[]
	dts = list(ohlcv.index)
	for dt in dts:
	    ohlcv_data = ohlcv.loc[dt].to_dict()
	    orderflow_data = profile[profile['t'] == dt][['p', 'q', 'd', 'b', 'a']].to_numpy()
	    print(ohlcv_data)
	    print(orderflow_data)
	    mp_slices.append(MarketProfileSlice(inst, dt, ohlcv_data, orderflow_data))

	plotter = OrderflowPlotter(token, interval, increment, ohlcv, mp_slices)
	plotter.orderflow_plot()
	plotter.show()
