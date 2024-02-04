# fastapi-chatbot

This chatbot application integrates [LaMini-LM](https://arxiv.org/abs/2304.14402) with a FastAPI backend and Streamlit frontend.

## Getting Started

Begin by downloading **ALL** necessary files from the [LaMini-LM model page on Hugging Face](https://github.com/jye-lim/fastapi-chatbot/tree/main/backend/model). Ensure these files are placed within the `model` directory located here: [Model Folder](https://github.com/jye-lim/fastapi-chatbot/tree/main/backend/model).

![model_page](https://github.com/jye-lim/fastapi-chatbot/blob/main/assets/model_page.png?raw=true)

## Running the App

To get your chatbot application up and running, follow these steps:

1. **Docker Setup**:
    - Ensure Docker is installed on your system. If not, download and install it from the [official Docker website](https://www.docker.com/get-started).
    - Navigate to the root directory of the project where the `docker-compose.yml` file is located.

2. **Build and Run the Docker Containers**:
    - Execute the following command in your terminal:
      ```
      docker compose up --build
      ```
    - This command builds the Docker images and starts the containers necessary for the application.

3. **Understanding IP Addresses**:
    - When Streamlit runs within the Docker container, it may print an IP address to the console. **Important:** This address is internal to the Docker container and is not the correct address to access the application externally.
    - To access the application, you need to find your machine's network IP address.

4. **Obtaining the Network IP Address**:
    - Use the `ifconfig` command on Unix-based systems or `ipconfig` on Windows to find your network IP address.
    - Look for an IP address under the `inet` field that is different from `127.0.0.1`.

5. **Accessing the Application**:
    - Open your web browser.
    - Enter your network IP address followed by `:8501` in the address bar (e.g., `192.168.1.2:8501`).
    - You should now see the FastAPI-Chatbot interface, ready for interaction!
