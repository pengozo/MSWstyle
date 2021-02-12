from yahoo_fin.stock_info import get_data
import matplotlib.pyplot as plt
import time

stocks=["LEGH","LOVE","LSEA","MESA","MGTA","MGTX","NMTR","OBNK","OPRA","ORTX","PAE","PRVB","QTT","REPL","ROAD","RUBY"] # Hier die Ticker rein

for stock in stocks:
    data = get_data(stock, start_date="01/21/2021", end_date="02/11/2021", index_as_date = True, interval="1d")  # Start und End datum setzten
    opens=data[["open", "high", "low"]]
    open_first = opens['open'].iloc[0]
    open_last = opens['open'].iloc[-1]
    gain =  (open_last - open_first)/open_first * 100
    
    
    if (gain > 20):
        print("Ticker:", stock, "Zuwachs %:" , gain)
        printer = stock + " - " + gain.astype(str)
        opens.plot(title=printer)
    time.sleep(1)   # Kein bock von Yahoo gebannt zu werden
