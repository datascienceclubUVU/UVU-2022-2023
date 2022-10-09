# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim

# Keeps Python from generating .pyc files in the container
EXPOSE 8501

# Turns off buffering for easier container logging
WORKDIR C:/Users/Chase/OneDrive/Documents/UVU-2022-2023/"Projects Hub"/"Fall 2022 Club Project"/Example

# Install pip requirements
RUN apt-get update && apr-get install -y \
    bui;d-essential \
    software_program-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/uvudataclub2022/UVU-2022-2023/blob/main/Projects%20Hub/Fall%202022%20Club%20Project/Example .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN pip3 install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT ["streamlit", "run", "user_behavior.py", "--server.port=8501", "--server.address=0.0.0.0"]
