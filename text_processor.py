"""

文本属性处理

"""


# 文本长度计数
def get_text_length(text: str):
    clean_text = text.strip()

    if not clean_text:
        return "文本内容为空，无法统计长度"

    return f"文本长度为：{len(clean_text)} 个字符"


# 文本词数计数
def get_text_word_count(text: str):
    """
    统计文本词数。
    这里采用按空白切分的轻量规则，适合英文或带空格的文本。
    """
    clean_text = text.strip()

    if not clean_text:
        return "文本内容为空，无法统计词数。"

    # 按空白切分词；中文连续文本暂时作为轻量近似处理
    word_count = len(clean_text.split())

    return f"文本词数约为：{word_count} 个"

# 文本句子数计数
def get_text_sentence_count(text: str):
    """
    统计文本句子数。
    这里用常见中英文句末标点做轻量判断。
    """
    clean_text = text.strip()

    if not clean_text:
        return "文本内容为空，无法统计句子数。"

    # 用常见中英文句末标点粗略统计句子数量
    sentence_endings = ["。", "！", "？", ".", "!", "?"]
    sentence_count = sum(clean_text.count(mark) for mark in sentence_endings)

    if sentence_count == 0:
        sentence_count = 1

    return f"文本句子数约为：{sentence_count} 句"
