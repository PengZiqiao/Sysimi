from langchain_tavily import TavilySearch
from langchain_community.tools import ShellTool

tavily_search = TavilySearch(
    max_results=5,
    topic="general",
    include_answer=False,
    include_raw_content=False,
    include_images=False,
    search_depth="basic"
)

shell_tool = ShellTool()

tools = [tavily_search, shell_tool]
