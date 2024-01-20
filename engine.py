import yfinance as yf
from pandas_datareader import data as pdr
yf.pdr_override()
import datetime as dt
import numpy as np
import pandas as pd
import math
from scipy.stats import gaussian_kde
from scipy.integrate import quad

class Engine:
    def __init__(self, root: str):
        self.pnl = 0

    def pnl_option_to_expiry(self, entry: float, strike: float, exp: dt.date, direction: int):
        self.pnl