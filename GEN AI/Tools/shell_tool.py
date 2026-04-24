from langchain_community.tools import ShellTool

shell_tool = ShellTool() # used to run commands in command line

results = shell_tool.invoke("whoami")

print(results)