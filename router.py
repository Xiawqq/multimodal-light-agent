'''
路由模块
'''

# 判断使用哪个模态
def route_question(question: str):
    question = question.lower()

    if "视频" in question or "video" in question:
        return "video"
    elif "图" in question or "image" in question:
        return "image"
    else:
        return "text"


# 视频模态细分
def route_video_question(question: str):
    question = question.lower()

    if "多长" in question or "时长" in question or "多久" in question or "duration" in question:
        return "duration"
    elif "多少帧" in question or "帧数" in question or "frame" in question:
        return "frame_count"
    else:
        return "summary"