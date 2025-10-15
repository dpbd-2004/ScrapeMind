# ScrapeMind: AI-Powered Web Scraper

ScrapeMind is an intelligent web scraping tool that leverages the power of large language models (LLMs) to parse and extract data from any website using natural language queries. Built with Python, Streamlit, Selenium, and Ollama, this application provides a simple web interface to turn unstructured web content into structured data.

![ScrapeMind Demo] https://lh3.googleusercontent.com/gg/AAHar4dYr09CW1AD9hQ_oNPdbNKxvCZjiboCXkhtESOePJhSCg7yrRzZvuiIbBmDBc-urY-4SMnDVjTlVQsXpyqXS4HLY0Z8cOCZdikw362-ImI1U01I2lX_53Y4mQxw1oTCLSNvPdNWGgQGEXfsPp7jVXlYHqJr4Y_r_WidGzWs7BSMY3KYHU5GDQQqzhGq74Ei-4n1Oo-YwUYnNJPtvm9osuwWSCi9vDAl_NvBdapkdM3SQrRTwJCvLF4uGB10qKNPp5gYNOe0JpjptKlq2uf1CsEumRKvTgE9aQ=d
## ✨ Features

-   **Scrape Any Website**: Input any URL to fetch its complete DOM content.
-   **Robust Scraping Engine**: Utilizes Bright Data's Browser API to handle dynamic content, bypass CAPTCHAs, and avoid IP blocks.
-   **Intelligent Parsing with AI**: Use natural language to ask for the specific data you need (e.g., "create a table of all products and their prices").
-   **Local LLM Support**: Powered by **Ollama**, allowing you to run powerful models like Llama 3 locally and for free.
-   **Interactive Web UI**: A simple and user-friendly interface built with **Streamlit**.

## 🛠️ Technologies Used

-   **Frontend**: Streamlit
-   **Scraping**: Selenium, Bright Data
-   **HTML Parsing**: BeautifulSoup4
-   **AI & LLM**: Ollama, LangChain
-   **Programming Language**: Python

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

1.  **Python 3.8+**
2.  **Ollama**: You must have Ollama installed and running on your machine.
    -   [Download Ollama](https://ollama.com/)
    -   After installing, pull a model to use for parsing (Llama 3 is recommended for a balance of speed and power):
        ```bash
        ollama pull llama3
        ```
3.  **Bright Data Account**: This project uses Bright Data's Browser API for robust scraping.
    -   Sign up for a [free trial account](https://brightdata.com/).

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/ScrapeMind.git](https://github.com/your-username/ScrapeMind.git)
    cd ScrapeMind
    ```

2.  **Create a Virtual Environment**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    -   Create a new file in the root of your project named `.env`.
    -   Log in to your Bright Data account, navigate to the **"Web Access"** tab, and create a **"Browser API"** zone.
    -   Go to the **"Access parameters"** for your new zone and copy the Selenium connection string.
    -   Add the connection string to your `.env` file:
        ```env
        SBR_WEBDRIVER="https://brd-customer-YOUR_USERNAME-zone-YOUR_ZONE:YOUR_PASSWORD@brd.superproxy.io:9515"
        ```

### Usage

With your virtual environment activated and Ollama running in the background, start the Streamlit application:

```bash
streamlit run main.py
