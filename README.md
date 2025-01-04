# AI-Powered Content Generator

Welcome to the AI-Powered Content Generator! This project is designed to help you create high-quality articles, blog posts, and other types of content using cutting-edge large language models (LLMs). By simply providing a keyword or topic, the generator crafts relevant and engaging content in seconds.

## Table of Contents

- [Overview](#Overview)
- [Features](#Features)
- [Technologies Used](#Technologies-Used)
- [Installation](#Installation)
- [Configuration](#Configuration)
- [Usage](#Usage)
- [Project Structure](#Project-Structure)
- [Deployment](#Deployment)
- [Contributing](#Contributing)
- [License](#License)
- [Acknowledgments](#Acknowledgments)

## Overview

This AI-powered content generator leverages Cohere's large language model API to generate high-quality content from simple inputs. The app is built using Python and deployed on Streamlit Cloud, making it accessible through a web interface.
You can interact with the app here: [AI-Powered Content Generator](https://build-your-own-ai-powered-content-generator-byxexx7m9nuwj67py7.streamlit.app/)

## **Below is a demonstration of the app's interface:**
![image](https://github.com/user-attachments/assets/172f6194-d674-4032-ad64-cd7ab15f71ff)


## Features

- Content Generation: Automatically generates articles and blog posts based on user input.

- Customizable Output: Define parameters such as keywords, tone, and length to tailor the generated content.

- Web Deployment: Deployable on Streamlit Cloud for easy access.

- User-Friendly Interface: Simple and intuitive front-end built with Streamlit.

## Technologies Used

- Python: Main programming language.

- Streamlit: Used to build the web interface.

- Cohere API: Provides the large language model for text generation.

- GitHub: Version control and code hosting.


## Installation

To run this project locally, follow the steps below:

1. Clone the repository:

``` bash
$ git clone https://github.com/aljebraschool/Build-Your-Own-AI-Powered-Content-Generator.git
$ cd Build-Your-Own-AI-Powered-Content-Generator

```

2. Create a virtual environment:

``` bash
# On Linux/Mac:
$ python3 -m venv venv
# On Windows:
$ python -m venv venv

```
3. Activate the virtual environment:

``` bash
# On Linux/Mac:
$ source venv/bin/activate
# On Windows:
$ venv\Scripts\activate

```

4. Install dependencies:

``` bash
$ pip install -r requirements.txt
```

## Configuration

1. Setting Up the API Key

2. Create a folder named .streamlit in the project directory.

3. Inside the .streamlit folder, create a file named secrets.toml.

4. Add the following line to secrets.toml:

``` bash
[api_keys]
cohere_api_key = "your_cohere_api_key_here"

```
Replace your_cohere_api_key_here with your actual Cohere API key.

## Usage

1. Run the application:

``` bash
$ streamlit run app.py

```

2. Access the app in your browser at http://localhost:8501.

3. Enter the desired keyword or topic and click the "Generate" button to create content.

## Project Structure

```plaintext
Build-Your-Own-AI-Powered-Content-Generator/
│
├── app.py                 # Main application logic
├── requirements.txt       # Project dependencies
├── .streamlit/            # Configuration folder
│   └── secrets.toml       # API key storage
├── .gitignore             # Files to ignore in version control
└── README.md              # Project documentation

```

## Deployment

# Deploying to Streamlit Cloud

1. Push the project to GitHub:

``` bash
$ git add .
$ git commit -m "Initial commit"
$ git push origin master
```
2. Log in to Streamlit Cloud and connect your GitHub account.

3. Click on "New App" and select the repository.

4. In "Advanced Settings," paste the contents of your secrets.toml directly.

5. Click "Deploy." Your app will be live and accessible via a public URL.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to Cohere for providing the language model API.

Inspired by the need to simplify content creation with AI.

  

