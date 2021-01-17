import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import flask
import plotly.express as px
import numpy as np
import pandas as pd

# From Python Cookbook
import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

def get_prime_distribution(n):
    hist, bins = np.histogram(get_primes_erat(n), bins=np.linspace(1.5, n-0.5, n-1))
    prime_count = np.cumsum(hist)
    return prime_count

max_int = 1000
df = pd.DataFrame()
integers = list(range(2, max_int))
df['Integers'] = integers
df['Prime Counting Function'] = integers/np.log(integers)
df['Number of Primes'] = get_prime_distribution(max_int)
fig = px.line(df, x="Integers", y=["Prime Counting Function", "Number of Primes"])

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True

quote = "In number theory, the prime number theorem (PNT) describes the asymptotic distribution of the prime numbers among the positive integers. It formalizes the intuitive idea that primes become less common as they become larger by precisely quantifying the rate at which this occurs."

app.layout = html.Div(
    children=[
        html.H1(children="Prime Number Theorem"),
        html.Div(children="""{}""".format(quote)),
        dcc.Graph(
            id="example-graph",
            figure=fig,
        ),
    ]
)


if __name__ == "__main__":
    import os
    debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True
    app.run_server(host="0.0.0.0", port=8050, debug=debug)
