from classes import Page
import base64
import pandas as pd
import requests
import streamlit as st

#Streamlit start design
st.set_page_config(page_title="Word Counter")
st.title("***Word Counter***", anchor=None)

#Variables
url_input = st.text_area("Enter full URLs here. Maximum of 60 URLs. (ex. https://currentdomain.com/current-page)", height=200)
url_input = url_input.split()
submit_button = st.button(label='Get word count')
count = 0
my_bar = st.progress(count)
word_count = []

#Streamlit logic
if submit_button:    
    if len(url_input) > 60:
        st.warning("Enter up to 60 URLs only")
    else:
        for element in url_input:
            word_count.append(Page(element).word_count())
            count += 1 / len(url_input)
            my_bar.progress(round(count,3))
                
        #DataFrame creation
        results = list(zip(url_input, word_count))
        df = pd.DataFrame(results)
        df.columns = ["URL", "Word Count"]
        df.index = df.index + 1
        st.table(df)
        csv = df.to_csv()
        b64 = base64.b64encode(csv.encode()).decode()
        st.markdown('### **⬇️ Download output CSV File **')
        href = f"""<a href="data:file/csv;base64,{b64}">Download CSV File</a> (Right-click and save as "filename.csv". Don't left-click)"""
        st.markdown(href, unsafe_allow_html=True)
