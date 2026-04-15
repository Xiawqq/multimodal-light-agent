def route(question):
    if "干什么" in question:
        return "action"
    elif "什么时候" in question:
        return "time"
    else:
        return "unknown"