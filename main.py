from bs4 import BeautifulSoup
from io import StringIO 
import streamlit as st
import pandas as pd
import requests
import base64

#Streamlit start design
st.set_page_config(page_title="Word Counter")
st.title("***Word Counter***", anchor=None)

#Word count function
def get_word_count(argument):
    full_url = argument
    page_source = requests.get(full_url).text
    soup = BeautifulSoup(page_source, 'lxml')
    paragraph_list = [element.text for element in soup.find_all('p')]
    word_count = len(str(paragraph_list).split())
    return word_count

#Variables
url_input = st.file_uploader(label="Upload a .TXT file with up to 50 URLs only. No HEADERS.", type='txt', accept_multiple_files=False)
count = 0
my_bar = st.progress(count)
word_count = []

#Streamlit logic
if url_input:
    bytes_data = StringIO(url_input.getvalue().decode("utf-8"))
    url_list = [element.strip() for element in bytes_data]
    
    if len(url_list) > 50:
        st.warning("Upload up to 50 URLs only")
    else:
        for element in url_list:
            word_count.append(get_word_count(element))
            count += 1 / len(url_list)
            my_bar.progress(round(count,3))
                
        #DataFrame creation
        results = list(zip(url_list, word_count))
        df = pd.DataFrame(results)
        df.columns = ["URL", "Word Count"]
        df.index = df.index + 1
        st.table(df)
        csv = df.to_csv()
        b64 = base64.b64encode(csv.encode()).decode()
        st.markdown('### **⬇️ Download output CSV File **')
        href = f"""<a href="data:file/csv;base64,{b64}">Download CSV File</a> (Right-click and save as "filename.csv". Don't left-click)"""
        st.markdown(href, unsafe_allow_html=True)
