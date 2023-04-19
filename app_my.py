import streamlit as st
import pandas as pd
st.write("""
# Find Highest number
""")
#Get Input
st.subheader('Please enter positive number')
st.header('User Input Parameters')

def user_input_features():
    number1 = st.number_input("Number 1",min_value=0.0)
    number2 = st.number_input("Number 2",min_value=0.0)
    number3 = st.number_input("Number 3",min_value=0.0)
    data = {'Number 1': number1,
            'Number 2': number2,
            'Number 3': number3
           }
    numbers = pd.DataFrame(data, index=[0])
    return numbers
df = user_input_features()
st.subheader('User Input parameters')
#st.write(df.to_dict())
for col in df.columns:
    if df[col].dtype != 'float64':
        df[col] = df[col].values.astype('float64')
n1=df['Number 1'][0]
n2=df['Number 2'][0]
n3=df['Number 3'][0]
count=0
if n1>n2 and n1>n3:
    st.write('Number 1 is the Greatest of all three numbers')
    count=1
if n3>n2 and n3>n1:
    st.write('Number 3 is the Greatest of all three numbers')
    count=1
if n2>n3 and n2>n1: 
    st.write('Number 2 is the Greatest of all three numbers')
    count=1
if (n2==n3 or n2==n1 or n1==n3) and count!=1:
    st.write('Please enter distinct Numbers')
