import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')

st.header('venta de vehículos')
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('datos variados de coches')
    fig = px.histogram(car_data, x="cylinders")
    st.plotly_chart(fig, use_container_width=True)
    
disp_button = st.button('modelos')
fig = px.scatter(car_data, x="model", y="model_year")
fig.show()

data_df = pd.DataFrame(
    {
        "model": car_data["model"],
        "price": car_data["price"],
    }
)

st.data_editor(
    data_df,
    column_config={
        "price": st.column_config.NumberColumn(
            "Price (in USD)",
            help="The price of the product in USD",
            min_value=3000,
            max_value=40000,
            step=1,
            format="$%d",
        )
    },
    hide_index=True,
)
