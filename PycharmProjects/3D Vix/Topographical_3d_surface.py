import ssl
import certifi

import pandas as pd
import plotly.graph_objects as go

ssl_context = ssl.create_default_context(cafile=certifi.where())

# Read data from URL with certifi SSL context
url = 'https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv'
z_data = pd.read_csv(url)

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title=dict(text='Mt Bruno Elevation'), autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
