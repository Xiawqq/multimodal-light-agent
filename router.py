def route_question(question: str):
    question = question.lower()

    if "视频" in question or "video" in question:
        return "video"
    elif "图" in question or "image" in question:
        return "image"
    else:
        return "text"