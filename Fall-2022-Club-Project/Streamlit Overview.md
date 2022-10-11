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
### <ins>Write</ins>
##### - This is the equivalent of Python's "print()" method and is used to display a line of text. To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
    streamlit.write('[string]')
#### CODE SAMPLE:
    import streamlit as st
    
    # write a basic line of text
    
    st.write('Hello, World!')
### <ins>Text</ins>
##### - This method is almost identical to the "write" method, with one minor difference: This method is primarily used to create blank spaces between headers and paragraphs. To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
    streamlit.text('[text]')
#### CODE SAMPLE:
    import streamlit as st
    
    # create blank space between lines of text.
    
    st.write('Welcome to my App!')
    st.text('')
    st.text('')
    st.write('Here is a brief description:')
### <ins>Set Page Configuration</ins>
##### - This method is used to set the page title and the app's structure. You can select between the default setting, "centered", or "wide". "Centered" is used to simply center your app's contents on the web page, whereas "wide" is used to fill the entire web page and is dynamic according to screen size*. To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
    streamlit.set_page_config(page_title='[title]', layout='[centered | wide]')
#### CODE SAMPLE:
    import streamlit as st
    
    # set page configuration
    
    st.set_page_config(page_title='My App', layout='centered')
### <ins>Markdown</ins>
##### - This method is used to create an internal CSS file that can be used to format text across your app. In order to activate the CSS, make sure to set the "unsafe_allow_html" parameter to "True". To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
    streamlit.markdown(''' <style>
                            .[class1] { [attribute1]: [value1];}
                            .[class2] { [attribute1]: [value1];
                                        [attribute2]: [value2];}
                            </style
                       ''', unsafe_allow_html=[True | False])
#### CODE SAMPLE:
    import streamlit as st
    
    # create internal CSS file
    
    st.markdown(''' <style>
                    .title { font-size: 45px;
                             text-align: center;}
                    .citation { font-size: 12px;
                                text-align: left}
                    </style>
                ''', unsafe_allow_html=True)
### <ins>Header</ins>
##### - Although headers can be created by using the "markdown" method as described above, the header object can be used to specify the titles of other objects including sidebars, expanders, and containers (all described below). To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
    streamlit.header('[header]')
#### CODE SAMPLE:
    import streamlit as st
    
    # create basic section header
    
    st.header('Description')
### <ins>Select Box</ins>
##### - This object allows users to select an item from a dropdown menu. In the example app, the drop down values are derived from the data warehouse that is being queried by the database engine. To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
    streamlit.selectbox(label='[label]', options=['list of values'], placeholder='[placeholder text]')
#### CODE SAMPLE:
    import streamlit as st
    
    # create select box for users to choose a color
    
    st.selectbox(label='Choose a Color:', options=['Red', 'Blue', 'Green', 'Yellow'], placeholder='Select a color...')
### <ins>Sidebar</ins>
##### - This object allows you to better organize your app's interactive features by grouping the interactive objects (such as Select Boxes) into a container that can be expanded and collapsed. To use this feature, follow the syntax below and use the following code sample:
#### SYNTAX:
    streamlit.sidebar.[element name]
    OR
    with streamlit.sidebar:
        streamlit.[element name]
        streamlit.[element name]
#### CODE SAMPLE
    import streamlit as st
    
    # create sidebar using the first syntax
    
    st.sidebar.header("Select your Vehicle's Options")
    st.sidebar.selectbox('Make:', options=['Ford', 'Chevrolet', 'Toyota'])
    st.sidebar.selectbox('Model:', options=['Explorer', 'Silverado', 'Tundra'])
    
    # create sidebar using the second syntax
    
    with st.sidebar:
        st.header("Select your Vehicle's Options")
        st.selectbox('Make:', options=['Ford', 'Chevrolet', 'Toyota'])
        st.selectbox('Model:', options=['Explorer', 'Silverado', 'Tundra'])
