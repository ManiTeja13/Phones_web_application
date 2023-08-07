import streamlit as st
import pandas as pd

# Sample mobile data in a Pandas DataFrame
# Replace this with your actual DataFrame
mobile_data = pd.read_csv("phones.csv")

def filter_mobiles(data, brand, color, storage, rating, screen_size, battery, price_range):
    filtered_data = data[
        (data['Brand'] == brand) &
        (data['Color'] == color) &
        (data['Storage'] == storage) &
        (data['Rating'] >= rating) &
        (data['Screen_size'] >= screen_size) &
        (data['Battery'] >= battery) &
        (data['Price'].between(price_range[0], price_range[1]))
    ]
    return filtered_data

def main():
    st.title('Mobile Finder App')

    # User inputs
    brand = st.selectbox('Brand', mobile_data['Brand'].unique())
    color = st.selectbox('Color', mobile_data['Color'].unique())
    storage = st.selectbox('Storage', mobile_data['Storage'].unique())
    rating = st.slider('Minimum Rating', 0.0, 5.0, 4.0, step=0.1)
    screen_size = st.slider('Minimum Screen Size', 4.0, 7.0, 5.0, step=0.1)
    battery = st.slider('Minimum Battery (mAh)', 2000, 6000, 3000, step=100)
    price_range = st.slider('Price Range', 0, 150000, (0,10000), step=50)

    # Filter mobiles based on user inputs
    filtered_mobiles = filter_mobiles(mobile_data, brand, color, storage, rating, screen_size, battery, price_range)

    if not filtered_mobiles.empty:
        st.subheader('Filtered Mobiles:')
        st.dataframe(filtered_mobiles)
    else:
        st.warning('No mobiles found matching the given criteria.')

if __name__ == '__main__':
    main()
