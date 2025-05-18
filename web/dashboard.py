from fastapi import FastAPI
import plotly.graph_objects as go

app = FastAPI()

@app.get("/chart")
async def generate_chart(df):
    fig = go.Figure(data=[
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close']
        ),
        go.Scatter(
            x=df.index,
            y=df['1x1'],
            name='Gann 1x1'
        )
    ])
    return fig.to_json()