import tools
import streamlit as st

#Title of app
st.title('Weather App')

with st.container():
    #Subheader for app - descripton
    st.subheader("This application will generate weather information based on user input for the current day")
    #Search param used for API call
    input = st.text_input('Input your town or city | Example: Gainesville, FL', '')
    #Displays search input
    st.write('The current location is', input)
    #Button used to call API function
    genButton = st.button('Generate')
    #If button is clicked All API - Display generated data
    try:
        if genButton:
            st.header("Forcast")
            data = tools.getweather(input)
            dataList = data.split(",")
            for d in dataList:
                st.write(d)
    except:
        st.write(f'Error getting data from API for the search term: {input}')    
        
   
        