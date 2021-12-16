from flask import Flask, render_template, request, send_from_directory, jsonify
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

application = Flask(__name__)
app = application

url ='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'

@app.route("/", methods=["GET","POST"])
def home():
    if request.args.get('f'):
        f = int(request.args.get('f'))
    else:
        f=15
    if request.args.get('q'):
        q = request.args.get('q')
    else:
        q = """
        {token (id:"0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"){tokenDayData{priceUSD date}}}
        """
    r = requests.post(url, json={'query': q})
    json_data = json.loads(r.text)
    df_data = json_data['data']['token']['tokenDayData']
    df = pd.DataFrame(df_data)
    df.priceUSD = df.priceUSD.replace(0, np.nan).dropna()
    df.priceUSD = df.priceUSD.astype(float)

    model = ARIMA(df.priceUSD, order=(1,1,0))
    fitted = model.fit()
    # Forecast
    fc = fitted.forecast(f)

    fc_series = pd.Series(fc)
    return jsonify({'predictions': list(fc_series)})

if __name__ == "__main__":
    app.run(debug=True)