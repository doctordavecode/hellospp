# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:35:56 2023

@author: user
"""

import streamlit as st

import os 
import openai

st.header("I can not catch me IT")
st.markdown("Questions?")
question = st.text_area("")
button = st.button("get your solution")

def play_tricks(question):
    openai.api_key="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"
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt= f"""{question}""",
        temperature=0.9,
        max_token=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text

if question and button:
    with st.spinner("Serving for you master, please wait...."):
        try:
            reply=play_tricks(question)
            st.markdown(reply)
        except:
            st.text('Master I am tired')