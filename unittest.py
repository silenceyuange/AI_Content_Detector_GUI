def main():
    import streamlit as st
    
    # Initialize session state if it does not exist
    if 'started' not in st.session_state:
        st.session_state.started = False
    
    if not st.session_state.started:
        if st.button("Get Started"):
            st.session_state.started = True
    
    if st.session_state.started:
        text = st.text_area("Type your text here")
        if st.button("Detect Text"):
            result = predict(text)
            st.write(result)
