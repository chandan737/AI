def get_waether():
  return "Today weather is suuny "

def draft_email():
  return "Email drafted : 'Hello , this is a test email.'"

tools = {
    "weather" : get_waether,
    "email" : draft_email
}

def langchain_style_agent(task):
  for keyword, tool in tools.items():
    if keyword in task:
      return tool()
  return "i don't know how to handle that yet "

print(langchain_style_agent("Check weather"))
print(langchain_style_agent("send an email"))
print(langchain_style_agent("unknow "))
