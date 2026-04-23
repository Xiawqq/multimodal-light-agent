import llm_interface


# 根据工具执行结果生成最终回答
def generate_answer(task_detail: str, result):
    # 使用 LLM 对结果进行自然语言重写
    rewritten_result = llm_interface.rewrite_answer(result)

    if task_detail == "duration":
        return f"系统回答：{rewritten_result}"

    elif task_detail == "frame_count":
        return f"系统回答：{rewritten_result}"

    elif task_detail == "motion":
        return f"系统回答：{rewritten_result}"

    elif task_detail == "change_time":
        return f"系统回答：{rewritten_result}"

    elif task_detail == "summary":
        return f"系统回答：{rewritten_result}"

    elif task_detail == "content":
        return f"系统回答：{rewritten_result}"

    else:
        return f"系统回答：{rewritten_result}"