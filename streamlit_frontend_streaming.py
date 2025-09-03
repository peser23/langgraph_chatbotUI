import streamlit as st
from langgraph_backend import workflow
from langchain_core.messages import HumanMessage, AIMessage

if "message_history" not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    if message['role'] == "user":
        with st.chat_message(name='user'):
            st.text(message['content'])
    if message['role'] == "assistant":
        with st.chat_message(name='assistant'):
            st.text(message['content'])

user_input = st.chat_input('Type Here')
CONFIG = {'configurable': {'thread_id': "1"}}
if user_input:
    st.session_state['message_history'].append({'role': "user", 'content': user_input})
    with st.chat_message(name='user'):        
        st.text(user_input)

    stream = workflow.stream(
        {'messages': [HumanMessage(content=user_input)]}, 
        config=CONFIG,
        stream_mode='messages') 
    with st.chat_message(name='assistant'):
        ai_message = st.write_stream(message_chunk for message_chunk, metadata in stream)

    st.session_state['message_history'].append({'role': "assistant", 'content': ai_message})  