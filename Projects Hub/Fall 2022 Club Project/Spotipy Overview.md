# Spotipy Overview
## Description
#### Spotitpy is a Python library that allows users to easily access Spotify's web servers and its publicly-accessible data. This library is primarily used for extracting data using Spotify's API for Web Developers and will be this project's primary data source.
## Library Features
#### As mentioned above, Spotipy offers a variety of tools to extract a variety of data from Spotify's web servers. Listed below are some of the methods and functions we will be using in this project to extract the appropriate data:
      * SpotifyClientCredentials (from spotipy.oauth2)
            - This is a class of methods and functions offered by Spotipy to access the Spotify API using a user's 
              embedded API key and Secret Key for authorized access. To use this feature, use the following code sample:
                  If you haven't installed Spotipy:
                    pip install Spotipy
                  If you have installed Spotipy, continue with the following code:
                    import Spotipy
                    from spotipy.oauth2 import SpotifyClientCredentials
                    
                    # create variables to hold credentials
                    cliend_id = '[copy and paste your client ID into this string]'
                    secret_key = '[copy and paste your secret key into this string]'
                    
                    # create variable to access the credentials manager function
                    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=secret_key)
                    
                    # assign the connection string to a simple variable
                    sp = Spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        * audio_features (using the "sp" variable from above)
             - This method accesses the connection variable we setup in the previous code sample to retrieve the audio features
               of a specified track. This method will retrieve all the metrics used for our analysis (e.g., instrumentalness, 
               acousticness, dancability). To use this feature, use the following code sample:
                    sp.audio_features([track uri])
        * track (using the "sp" variable from above)
             - This method retrieves all relevant track information from Spotify's Data Warehouse via the Spotify API connection
               we created earlier. Because web data is stored in JSON files, we need to specify the paths in order to retrieve
               the data related to our inquiry (see Pandas overview for more information). To use this feature, use the following
               code sample:
                    sp.track([track uri])
