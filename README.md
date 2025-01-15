# Agentic AI with Phi playground

This repository contains a Python-based application that leverages the Phi framework to create a web-based interactive playground with two specialized agents:

1. **Web Search Agent**: Utilizes Groq's Llama3 model and DuckDuckGo search tools to fetch real-time web information with sources.
2. **Financial AI Agent**: Provides financial insights using YFinanceTools, such as stock prices, analyst recommendations, and company news.

## Features
- **Web Search Agent**: Performs web searches using DuckDuckGo and returns summarized results with source links.
- **Financial AI Agent**: Fetches financial data such as stock prices, fundamentals, and news in a structured tabular format.
- **Interactive Playground**: Users can interact with the agents through a web-based UI powered by the Phi Playground.

## Requirements
- Python 3.9+
- [Phi](https://docs.phi.ai/)
- [Groq](https://groq.com/)
- `dotenv` for managing environment variables

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Phi API key and Groq API key:
   ```
   PHI_API_KEY=your_api_key_here
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Access the web interface at:
   ```
   https://www.phidata.app/playground/chat
   ```
   Select the endpoint

## Code Overview

- **`app.py`**: Main script to launch the playground app.
- **Agents**:
  - `Web Search Agent`: Searches the web for financial information using DuckDuckGo.
  - `Financial AI Agent`: Provides financial insights from YFinanceTools.

## Example Interactions

### Web Search Agent
- Query: "Latest news on Tesla stock"
- Output: Summarized news articles with source links.

### Financial AI Agent
- Query: "AAPL stock price"
- Output: Current stock price, fundamentals, and latest news in tabular format.

### Both
- Query: Compare Tesla and NVIDIA and provide analyst recommendation. What should I buy? (TRY THIS OUT!!!)
