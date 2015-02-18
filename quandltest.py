import Quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pull from config.py - you need to create your own with authtoken = "YOUR QUANDL KEY"
import config
authtoken = config.authtoken

trim_start="2014-01-01"
# trim_end="yyyy-mm-dd" # Not used so data is pulled up to current day

# Pull data from Quandl
WTI = Quandl.get("DOE/RWTC", authtoken=authtoken, transformation="normalize", trim_start=trim_start)
USO = Quandl.get("GOOG/NYSE_USO", authtoken=authtoken, transformation="normalize", trim_start=trim_start)
DBO = Quandl.get("GOOG/NYSE_DBO", authtoken=authtoken, transformation="normalize", trim_start=trim_start)
DBE = Quandl.get("GOOG/NYSE_DBE", authtoken=authtoken, transformation="normalize", trim_start=trim_start)

# Attempt to automate these joins failing when trying to assign back to left hand data.
# x = x.join(y) does not seem to work but z = x.join(y) works
# dataList = [WTI,USO,DBO,DBE]
# cols = ["WTI","USO","DBO","DBE"]

# # Add the first two col names to cols
# # cols = [dataList[0].__name__,dataList[1].__name__]
# # Join the first two data items:
# all_data = dataList[0].join(dataList[1]['Close'])

# # Join the rest of the data items:
# for i in range(2,len(dataList)-1):
# 	# cols.append(dataList[i].__name__)
# 	all_data = all_data.join(dataList[i]['Close'])

# # Replace data column titles with what we want
# all_data.columns = cols

# This is ugly but it works:
first_join = WTI.join(USO['Close'])
first_join.columns = ['WTI', 'USO']
second_join = first_join.join(DBO['Close'])
second_join.columns = ['WTI', 'USO', 'DBO']
third_join = second_join.join(DBE['Close'])
third_join.columns = ['WTI', 'USO', 'DBO', 'DBE']

all_data = third_join

recent_data = all_data.tail(90)
recent_data.plot()
plt.savefig("recent.png", bbox_inches='tight')
plt.show()

all_data.plot()
plt.savefig("all_data.png", bbox_inches='tight')
plt.show()

# Other ETFs to track
"""USO	United States Oil Fund, LP	$19.62	+2.29%	$1,132,074	27,498,463	-3.63%
OIL	iPath Exchange Traded Notes S&P GSCI Crude Oil Total Return Index Medium-Term Notes Series A	$12.01	+2.91%	$736,354	3,334,829	-4.23%
UNG	United States Natural Gas Fund, LP	$14.22	+2.45%	$701,223	13,312,313	-3.72%
DBO	PowerShares DB Oil Fund	$14.88	+0.54%	$471,594	849,542	-5.22%
DBE	PowerShares DB Energy Fund	$17.43	+1.75%	$140,876	193,790	-0.23%
BNO	United States Brent Oil Fund	$23.05	+3.50%	$98,032	179,306	+1.54%
UGA	United States Gasoline Fund, LP	$36.56	+1.73%	$86,088	72,506	+7.06%
USL	United States 12 Month Oil Fund, LP	$26.81	+1.51%	$75,582	80,537	-0.04%
RJN	ELEMENTS Exchange Traded Notes Rogers International Commodity Index - Energy Total Return	$3.98	+2.31%	$26,984	145,508	-0.25%
UNL	United States 12 Month Natural Gas Fund	$13.33	+1.52%	$19,024	29,748	-3.48%
GAZ	iPath Dow Jones-UBS Natural Gas Subindex Total Return ETN	$1.44	-0.69%	$14,278	83,856	-28.36%
OLO	PowerShares DB Crude Oil Long ETN	$7.58	+0.26%	$10,956	26,955	-8.67%
TWTI	RBS Oil Trendpilot Exchange Traded Notes	$20.54	+0.05%	$6,573	1,238	+0.79%
UHN	United States Diesel-Heating Oil Fund	$23.32	+3.05%	$4,570	3,882	+8.06%
UBN	UBS E-TRACS CMCI Energy Total Return ETN	$10.14	+2.01%	$4,567	9,317	-1.36%
OLEM	iPath Pure Beta Crude Oil	$25.07	+1.21%	$3,314	2,425	+0.48%
JJE	iPath Exchange Traded Notes Dow Jones - AIG Energy Total Return Sub-Index ETN Series A	$10.42	+2.46%	$2,032	3,195	+2.46%
ONG	iPath Pure Beta Energy	$25.61	unch	$1,800	510	-1.91%
DCNG	iPath Seasonal Natural Gas	$20.81	-4.10%	$982	1,239	-7.22%
FUE	Elements Exchange Traded Notes MLCX Biofuels Index (Exchange Series)-Total Return	$8.25	-2.94%	$908	1,042	-5.93%
RGRE	RBS Rogers Enhanced Energy ETN	$16.73	+7.94%	$N/A	367	-3.46%"""
