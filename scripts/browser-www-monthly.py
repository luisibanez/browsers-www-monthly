# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# <codecell>

browsers = pd.read_csv('browser-ww-monthly-200812-201402.csv')

# <codecell>

somebrowsers = browsers[['IE','Firefox','Chrome','Safari','Opera']]
somebrowsers.plot()

