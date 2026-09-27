import streamlit as st

st.title('Stock Level Checker')
stock=st.number_input('Units in stock',min_value=0)

if st.button('Check Stock'):
    if stock==0:
        st.error('Out of Stock')
    elif stock<=5:
        st.warning('Low Stock')
    else:
        st.success('Stock Level is Healthy')





