<img src="./images/qdrant.png" width="125px"/>

# Qdrant Search API

<img src="./images/works-on-my-machine.svg" height="25px"/>

Simple Neural Search API for Qdrant

## Project Details

- Developed with Python version 3.10 and FastAPI
- Qdrant Client
- Sentence Transformer

## Getting Started

- Create a .env file and include the contents of the [.env.example](.env.example)

- To initialize a virtual enviroment, navigate to the 'src' directory in the terminal and execute

  ```
  $ python -m venv venv
  ```

- Activate the virtual environment, on MacOS or Linux with

  ```
  $ source venv/bin/activate
  ```

- Install dependencies

  ```
  $ pip install -r requirements.txt
  ```

- Run the service

  ```
  $ python service.py
  ```

  Open your browser at http://localhost:8000/docs

- To deactivate the virtual environment

  ```
  $ deactivate
  ```
