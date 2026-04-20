"""

文本属性处理

"""


# 文本属性处理的基础能力，适合作为 text 模态的第一个最小可执行能
def get_text_length(text: str):
    clean_text = text.strip()

    if not clean_text:
        return "文本内容为空，无法统计长度"

    return f"文本长度为：{len(clean_text)} 个字符"


# 文本属性处理的基础能力，适合作为 text 模态的第二个最小可执行能力
def get_text_stats(text: str):
    """
    统计文本的基础结构信息，包括词数和句子数。
    这里采用轻量规则，适合作为 text 模态的第二个最小可执行能力。
    """
    clean_text = text.strip()

    if not clean_text:
        return "文本内容为空，无法统计文本信息。"

    # 按空白切分词，适合英文或带空格的文本；中文场景先作为轻量近似
    word_count = len(clean_text.split())

    # 用常见中英文句末标点粗略统计句子数量
    sentence_endings = ["。", "！", "？", ".", "!", "?"]
    sentence_count = sum(clean_text.count(mark) for mark in sentence_endings)

    if sentence_count == 0:
        sentence_count = 1

    return f"文本统计结果：词数约为 {word_count}，句子数约为 {sentence_count}。"
