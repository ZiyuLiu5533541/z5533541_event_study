""" yf_example2.py
Example of a function to download stock prices from Yahoo Finance.
"""
import yfinance as yf
def yf_prc_to_csv(tic, pth, start=None, end=None):
 """ Docstrings
 """
 df = yf.download(tic, start=start, end=end, ignore_tz=True)
 df.to_csv(pth)
# Example
tic = 'QAN.AX'
pth = 'qan_stk_prc.csv'
yf_prc_to_csv(tic, pth)


print(f"The value of __name__ is: '{__name__}'")

if __name__ == "__main__":
 import os
 import toolkit_config as cfg
 tic = 'QAN.AX'
 pth = os.path.join(cfg.DATADIR, 'qan_stk_prc.csv')
 yf_prc_to_csv(tic, pth)
