from django.shortcuts import render
import pandas as pd
import plotly.express as px
# Create your views here.


def Dashboard(request):

    df = pd.read_csv(
        "https://raw.githubusercontent.com/subaash1112/Assured-Data-Science-FS/data/property2.csv",
        index_col=0,
    )

    # Chart 1
    df2 = df[(df["Property Type"] == "Condominium") & (df["Price"] <= 700000)]
    fig = px.pie(
        df2,
        values="Price",
        names="Location",
        title="Prices of condominium less than RM700,000"
        # height=800,
        # width=1200,
    )
    fig.update_traces(textposition="inside")
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode="hide")
    chart1 = fig.to_html

    # insert another chart here
    # Chart 2
    import plotly.graph_objects as go

    fig = go.Figure(go.Bar(x=df2["Location"], y=df2["Price"], name="Location"))

    fig.update_xaxes(
        showgrid=True, ticks="outside", tickson="boundaries", automargin=True
    )

    fig.update_layout(
        title="Property prices in round KL",
        xaxis_title="Location",
        yaxis_title="Price",
    )

    chart2 = fig.to_html

    # chart3
    high = df[df["Price"] > 20000000]
    fig = px.sunburst(
        high,
        path=["Location", "Property Type", "Furnishing"],
        values="Price",
        title="Prices of properties more than RM2,000,000.",
    )
    chart3 = fig.to_html()

    # # chart4
    import plotly.graph_objects as go

    df = pd.read_csv(
        "https://raw.githubusercontent.com/subaash1112/Assured-Data-Science-FS/data/property2.csv",
        index_col=0,
    )
    df.rename(columns={"Car Parks": "CarParks"}, inplace=True)
    df2 = df[["Location", "Price", "Rooms", "Bathrooms", "CarParks"]]

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(df2.columns), fill_color="paleturquoise", align="left"
                ),
                cells=dict(
                    values=[
                        df2.Location,
                        df.Price,
                        df.Rooms,
                        df.Bathrooms,
                        df.CarParks,
                    ],
                    fill_color="lavender",
                    align="left",
                ),
            )
        ]
    )
    chart4 = fig.to_html()

    context = {"chart1": chart1, "chart2": chart2,
               "chart3": chart3, "chart4": chart4}
    return render(request, "index.html", context)
