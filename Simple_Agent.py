def Simple_Agent(task):
  if "weather" in task:
    return "Agent : i will check the weather"
  elif "email" in task:
    return "Agent: Drafting and email"
  else:
    return "Agent: Task not recogined"
print(Simple_Agent("Check weather"))
