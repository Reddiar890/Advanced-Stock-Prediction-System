# -*- coding: utf-8 -*-
"""Advanced Stock Prediction System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11JmK9tqT7gWeFsm3DBXvckg0Km67RNpW
"""

# Commented out IPython magic to ensure Python compatibility.
# Data Imports
import yfinance as yf
import pandas as pd
import numpy as np
import random

from sklearn.preprocessing import MinMaxScaler
from pandas.tseries.offsets import BDay

# Visualization Imports
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import scipy.stats as stats

# Neural Network Imports
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras import regularizers
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Bidirectional
from tensorflow.keras.callbacks import ModelCheckpoint

# Setting seed
SEED = 0
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Visualization Configurations
pio.templates.default = "plotly_dark"
# %config InlineBackend.figure_format = 'retina'