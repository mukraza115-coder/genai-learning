from langchain_community.tools import DuckDuckGoSearchRun

#!used for websearch
search_tool=DuckDuckGoSearchRun()

result=search_tool.invoke("PSl headlines")

print(result)