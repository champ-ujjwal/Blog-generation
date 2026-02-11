import streamlit as st
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain_community.llms import CTransformers

# function to get respopnse from llama 2 model
def getLLamaresponse(input_text, no_words, blog_Style):
    # calling llama2 model
    llm=CTransformers(model='/home/ujjwal/LLama/models/llama-2-7b-chat.ggmlv3.q8_0.bin',model_type='llama',config={'max_new_tokens':256, 'temperature':0.7})

    # creating prompt template
    template="""
            write a blog for {blog_Style} in {no_words} words on the topic {input_text}
            """
    
    prompt=PromptTemplate(input_variables=["blog_Style","input_text","no_words"], template=template)

    # Generate the response
    response = llm(prompt.format(blog_Style=blog_Style, input_text=input_text, no_words=no_words))
    print(response)
    return response







st.set_page_config(page_title="Generate Blogs", page_icon=":robot_face:",layout="centered", initial_sidebar_state="collapsed")
st.header("Generate Blogs")

input_text=st.text_area("Enter your Blog content", height=200)
# creating two more columns for additional 2 fields

col1, col2 = st.columns([5,5])
with col1:
    no_words=st.number_input("Number of word")
with col2:
    blog_Style=st.selectbox("Writing the blog for", ("Researchers", "Students", "General Audience"), index=0)
submit=st.button("Generate Blog")


# final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_Style))