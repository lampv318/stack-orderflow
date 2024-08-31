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
type = sys.argv[2]

if __name__ == '__main__':
	inst = 'btcusdt'
	increment = 500
	token = inst.upper()
	interval = '1D'

	if type == 'day':
		ohlcv = pd.read_csv(f"./../datalake-vni/p_d/{stock}-pd.csv", index_col=0)
		profile = pd.read_csv(f"./../datalake-vni/stack_orderflow/{stock}-orderflow.csv")
	elif type == 'hour':
		ohlcv = pd.read_csv(f"./../datalake-vni/p_d_hour/{stock.upper()}-pd-hour.csv", index_col=0)
		profile = pd.read_csv(f"./../datalake-vni/stack_orderflow_hour/{stock.upper()}-orderflow.csv")

	profile['t'] = pd.to_datetime(profile['t'])
	ohlcv.index = pd.to_datetime(ohlcv.index)

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
