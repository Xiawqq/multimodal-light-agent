"""

文本属性处理

"""


def get_text_length(text: str):
    clean_text = text.strip()

    if not clean_text:
        return "文本内容为空，无法统计长度"

    return f"文本长度为：{len(clean_text)} 个字符"