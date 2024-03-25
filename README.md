# Riverscapes API Demo

## Working with this repo

You can clone this repo locally or use it inside Github Codespaces (which is much easier).

## `demo_search.py`

This demonstrates all the different ways you can search for things in the Riverscapes Data exchange API.

There are quite a few inline comments that explain what each part of the code does.

You will also see a description at the bottom of the file on how to instantiate the `RiverscapesAPI` class in two different ways.

To run this file open it in VSCode and select "Run and Debug" from the side menu then choose "Python: Current File"

## `file_download.py`

This is a more specific demo that shows how to download one single file from each project in a search result from the Riverscapes Data Exchange API.

To run this file open it in VSCode and select "Run and Debug" from the side menu then choose "Python: Current File"


## Other files/folders in this repo:

- `inputs/`: These are git-ignored files (except for the two demo examples) that you can use as inputs to your searches.
- `graphql/` This is where you will find a copy of the API Schema and a small sample of queries you can run. If you're using VSCode this repo should suggest installation of the 
- `riverscapesdemo/classes/RiverscapesAPI.py` This is a simple class that wraps a lot of API functionality to make querying the API easier in python. 
- `riverscapesdemo/classes/riverscapes_helpers.py` This is a file that contains some helper functions that are used in the `RiverscapesAPI` class. Objects coming back from the API are JSON so it's nice to convert them to more pythonic objects to save time, reduce parsing and make the code more readable.
- `.devcontainer`: This is a folder that contains the configuration for the Github Codespaces environment. It's a good idea to use this if you're working in a Codespace. It will install all the necessary extensions and tools you need to work with this repo.

## Recommended VSCode Extensions

- `GraphQL.vscode-graphql-syntax`: GraphQL for Visual Studio Code: Syntax highlighting and bracket matching for GraphQL.
- `GraphQL.vscode-graphql`: GraphQL extension for VSCode. When configured it will give you autocomplete on your graphql queries and schemas,

### Python Extensions

- `ms-python.autopep8`,
- `ms-python.pylint`,
- `ms-python.python`,
- `ms-python.vscode-pylance`,
- `njpwerner.autodocstring`,

### Other Extensions (mostly optional)

- `mhutchie.git-graph`: Git Graph: View a Git Graph of your repository, and perform Git actions from the graph,
- `redhat.vscode-xml`: XML Language Support by Red Hat,
- `yzhang.markdown-all-in-one`: Markdown All in One. Good for previewing markdown files,
- `GitHub.copilot-chat`: GitHub Copilot Chat: Chat with GitHub Copilot,
- `GitHub.copilot`: GitHub Copilot: Your AI pair programmer
- `ms-vsliveshare.vsliveshare`: Live Share: Real-time collaborative development from the comfort of your favorite tools,