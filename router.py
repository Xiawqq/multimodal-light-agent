"""

路由模块

"""


# 判断使用哪个模态
def route_question(question: str):
    question = question.lower()

    if "视频" in question or "video" in question:
        return "video"
    elif "图片" in question or "图像" in question or "照片" in question:
        return "image"
    else:
        return "text"


# 视频模态细分
def route_video_question(question: str):
    question = question.lower()

    if "多长" in question or "时长" in question or "多久" in question or "duration" in question:
        return "duration"

    elif "有多少帧" in question or "帧数" in question or "总帧数" in question:
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


# 图像模态细分
def route_image_question(question: str):
    if "多大" in question or "尺寸" in question or "宽高" in question:
        return "size"
    else:
        return "size"


# 文本模态细分
def route_text_question(question: str):
    question = question.lower()

    # 用户询问词数时，路由到词数统计工具
    if "词数" in question or "多少词" in question or "word count" in question:
        return "word_count"

    # 用户询问句子数量时，路由到句子数统计工具
    elif "句子数" in question or "多少句" in question or "sentence count" in question:
        return "sentence_count"

    # 默认仍然返回文本长度工具，保持原有行为稳定
    elif "多少字" in question or "长度" in question or "多长" in question:
        return "length"
    else:
        return "length"


# 按当前模态分发到对应的子任务路由函数
def route_task_detail(modality: str, question: str):
    """
    根据已经识别出的模态，继续路由到对应的子任务。
    这样主流程只需要知道当前模态，不需要自己判断该调用哪个 route_xxx_question。
    """
    if modality == "video":
        return route_video_question(question)
    elif modality == "image":
        return route_image_question(question)
    else:
        return route_text_question(question)
