from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
import streamlit as st

load_dotenv()

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
    # connceting to mysql db using mysql-connector-python  driver
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)


st.set_page_config(page_title="Chat with SQL", page_icon=":speech_ballon")
st.title("Chat with my MySQL")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application using LLM and MySQL")
    st.write("Connect to the databse and satrt chatting.")

    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", value="admin", key="Password")
    st.text_input("Database", value="World", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"],
            )
            st.session_state.db = db
            st.success("Connected to database!")

st.chat_input("Type a message...")