import streamlit as st

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
if user_input:
    with st.chat_message(name='user'):
        st.session_state['message_history'].append({'role': "user", 'content': user_input})
        st.text(user_input)

    with st.chat_message(name='assistant'):
        st.session_state['message_history'].append({'role': "assistant", 'content': user_input})
        st.text(user_input)