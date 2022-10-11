# Streamlit Overview
## Description
#### Streamlit is a Python library that allows users to design and deploy web apps via local hosting, Streamlit Cloud, or Docker Containers. This library is primarily used for Machine Learning and Data Visualization applications.
## Deploying Streamlit via localhost
#### As mentioned above, Streamlit allows users to deploy web apps via local hosting and other methods. To deploy your streamlit app via your local machine, complete the following steps:
1. Pip install streamlit
2. Download Anaconda Navigator
3. In Anaconda Navigator, Go to "Environments" > "Create New Environment"
    - Type in a unique name for your new environment
    - Make sure "Python 3.9" is selected
4. Run the New Environment by clicking on its title
5. Click on the play button and select "Open Terminal"
6. With the terminal open, type "cd [path]" (without the quotes) and copy and paste the file path to your app's Python file
7. With the new directory specified, type "streamlit run [file name].py" (without the quotes)
## Library Features
#### Streamlit allows users a wide variety of tools for interactivity, structure, and formatting for your web app. The tools used in the example app include the following:
#### <ins>Write</ins>
##### - This is the equivalent of Python's "print()" method and is used to display a line of text. To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
          streamlit.write('[string]')
#### CODE SAMPLE:
    import streamlit as st
    
    # write a basic line of text
    
    st.write('Hello, World!')
#### <ins>audio_features</ins> (using the "sp" variable from above)
##### - This method accesses the connection variable we setup in the previous code sample to retrieve the audio features of a specified track. This method will retrieve all the metrics used for our analysis (e.g., instrumentalness, acousticness, dancability). To use this feature, use the following code sample:
                    sp.audio_features([track uri])
#### <ins>track</ins> (using the "sp" variable from above)
##### - This method retrieves all relevant track information from Spotify's Data Warehouse via the Spotify API connection we created earlier. Because web data is stored in JSON files, we need to specify the paths in order to retrieve the data related to our inquiry (see Pandas overview for more information). To use this feature, use the following code sample:
                    sp.track([track uri])
