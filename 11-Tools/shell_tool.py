from langchain_community.tools import ShellTool

search=ShellTool()

result=search.invoke("Tools")

print(result)