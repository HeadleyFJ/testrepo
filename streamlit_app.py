import streamlit as st
import matplotlib.pyplot as plt

#create your figure and get the figure object returned
fig = plt.figure() 

x = [1,2,3,4,5]
y = [2,4,3,5,4]
plt.scatter(x,y) 

st.pyplot(fig)
