from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi
import phi.api
from phi.playground import Playground, serve_playground_app

import os
from dotenv import load_dotenv
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

# Web search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for financial information",
    model=Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Financial agent
financial_agent = Agent(
    name="Financial AI Agent",
    model=Groq(id="llama3-70b-8192"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Provide a valid stock symbol. Use tabular form to display data."],
    show_tool_calls=True,
    markdown=True
)

# Playground app
app = Playground(agents=[financial_agent, web_search_agent]).get_app()

# Run the app
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
