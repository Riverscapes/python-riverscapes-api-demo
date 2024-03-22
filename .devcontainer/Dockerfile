############################################################################################
# Dev Container for riverscapes-tools
############################################################################################
FROM mcr.microsoft.com/devcontainers/python:3.11 AS worker

# Some preliminary dependencies
RUN apt update && apt upgrade -y && apt autoremove -y

RUN apt-get install -y curl wget git build-essential libssl-dev gcc g++ make zsh vim \
                software-properties-common awscli locales

# Python stuff
RUN apt-get install -y python3-pip proj-data proj-bin \
              gdal-bin libgdal-dev libspatialindex-dev \
              python3-matplotlib

# Install NodeJS v18 
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g @riverscapes/cli

# Now follow up on python install
RUN pip install --upgrade pip

# Now install  18 
USER vscode
RUN wget https://raw.githubusercontent.com/Riverscapes/environment/master/nar-ys.zsh-theme -O ~/.oh-my-zsh/custom/themes/nar-ys.zsh-theme
RUN wget https://raw.githubusercontent.com/Riverscapes/environment/master/.aliases -O ~/.aliases
RUN wget https://raw.githubusercontent.com/Riverscapes/environment/master/.zshrc -O ~/.zshrc


WORKDIR /workspaces/python-riverscapes-api-demo
