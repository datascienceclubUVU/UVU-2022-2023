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
#### As mentioned above, Spotipy offers a variety of tools to extract a variety of data from Spotify's web servers. Listed below are some of the methods and functions we will be using in this project to extract the appropriate data:
#### <ins>Write</ins> (from spotipy.oauth2)
##### - This is a class of methods and functions offered by Spotipy to access the Spotify API using a user's embedded API key and Secret Key for authorized access. To use this feature, use the following code sample:
#### If you haven't installed Spotipy:
          pip install Spotipy
#### If you have installed Spotipy, continue with the following code:
    import Spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    # create variables to hold credentials
    cliend_id = '[copy and paste your client ID into this string]'
    secret_key = '[copy and paste your secret key into this string]'

    # create variable to access the credentials manager function
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=secret_key)

    # assign the connection string to a simple variable
    sp = Spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#### <ins>audio_features</ins> (using the "sp" variable from above)
##### - This method accesses the connection variable we setup in the previous code sample to retrieve the audio features of a specified track. This method will retrieve all the metrics used for our analysis (e.g., instrumentalness, acousticness, dancability). To use this feature, use the following code sample:
                    sp.audio_features([track uri])
#### <ins>track</ins> (using the "sp" variable from above)
##### - This method retrieves all relevant track information from Spotify's Data Warehouse via the Spotify API connection we created earlier. Because web data is stored in JSON files, we need to specify the paths in order to retrieve the data related to our inquiry (see Pandas overview for more information). To use this feature, use the following code sample:
                    sp.track([track uri])
