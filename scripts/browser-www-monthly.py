# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# <codecell>

# Read data from the local disk
# browsers = pd.read_csv('../data/browser-ww-monthly-200812-201402.csv')

# Or download it from StatCounter directly
browsers = pd.read_csv('http://gs.statcounter.com/chart.php?201402=undefined&device=Desktop%20%26%20Mobile%20%26%20Tablet%20%26%20Console&device_hidden=desktop%2Bmobile%2Btablet%2Bconsole&statType_hidden=browser&region_hidden=ww&granularity=monthly&statType=Browser&region=Worldwide&fromInt=200812&toInt=201402&fromMonthYear=2008-12&toMonthYear=2014-02&multi-device=true&csv=1')

# <codecell>

somebrowsers = browsers[['IE','Firefox','Chrome','Safari','Opera']]
somebrowsers.plot()

