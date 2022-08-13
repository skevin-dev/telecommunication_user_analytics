import streamlit as st
from multiapp import MultiApp
from dashboard import experience, overview, satisfactory # import your app modules here

app = MultiApp()

st.sidebar.markdown('# **Tellco Customers Analysis**')
st.sidebar.markdown("""
This project is all about analyzing TellCo's user and find out whether it is worth buying or selling.
""")

# Add all your application here
app.add_app("User Overview", overview.app)
app.add_app("User Experience", experience.app)
app.add_app("User Satisfaction", satisfactory.app)
# The main app
app.run()