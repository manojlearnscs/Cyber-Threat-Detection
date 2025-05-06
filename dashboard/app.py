import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:/Users/Manoj/Desktop/Cyber-Threat-Detection/data/network_traffic.csv')


# Display the dataset
st.write("Network Traffic Data")
st.write(df)

# Plot the bytes used per protocol
protocols = df.groupby('protocol')['bytes'].sum()

fig, ax = plt.subplots()
protocols.plot(kind='bar', ax=ax)
ax.set_title('Total bytes used per protocol')
ax.set_xlabel('Protocol')
ax.set_ylabel('Bytes')

st.pyplot(fig)
