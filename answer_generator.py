
def generate_answer(task_detail: str, result):
    if task_detail == "duration":
        return f"根据当前分析，{result}"

    elif task_detail == "frame_count":
        return f"根据当前分析，{result}"

    elif task_detail == "motion":
        return f"关于活动情况的判断如下：{result}"

    elif task_detail == "summary":
        return f"视频内容概括如下：{result}"

    elif task_detail == "content":
        return f"对视频内容的初步分析如下：{result}"

    else:
        return f"系统返回结果：{result}"