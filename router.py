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

    elif "多少帧" in question or "帧数" in question or "总帧数" in question:
        return "frame_count"

    elif "fps" in question or "帧率" in question or "每秒多少帧" in question:
        return "fps"

    elif "什么时候变化" in question or "何时变化" in question or "变化最明显" in question:
        return "change_time"

    elif "活动" in question or "运动" in question:
        return "motion"

    elif "主要内容" in question or "主要讲了什么" in question or "概括" in question:
        return "summary"

    else:
        return "content"