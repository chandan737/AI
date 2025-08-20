def get_waether():
  return "Today weather is suuny "

def draft_email():
  return "Email drafted : 'Hello , this is a test email.'"

def smart_agent(task):
  if "weather" in task:
    return get_waether()
  elif "email" in task:
    return draft_email()
  else:
    return "i don't know how to handle that yet "
print(smart_agent("Check weather"))
print(smart_agent("send an email"))
