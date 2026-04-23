"""
LLM 接口层

当前阶段先不直接接入真实大模型 API，
而是预留统一的 AI 能力入口，便于后续逐步替换规则逻辑。
"""


def rewrite_answer(result: str) -> str:
    """
    对工具执行结果进行自然语言重写。
    这是最适合作为第一步接入 LLM 的位置，因为它不会影响工具选择和执行流程。
    """
    return result


def understand_question(question: str) -> str:
    """
    预留问题理解入口。
    后续可以在这里接入 LLM，对用户问题做意图理解或补充解释。
    """
    return question


def choose_tool_with_llm(question: str, tools_schema: list[dict]) -> str:
    """
    预留 LLM 选工具入口。
    当前阶段先不做真实决策，只保留函数签名，方便后续接入。
    """
    return ""
