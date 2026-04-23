"""
LLM 接口层

当前阶段先不直接接入真实大模型 API，
而是预留统一的 AI 能力入口，便于后续逐步替换规则逻辑。
"""


import os


# 获取当前配置的 LLM provider
def get_llm_provider() -> str:
    """
    获取当前配置的 LLM provider。
    默认使用 mock，保证在没有真实 API 的情况下项目仍可运行。
    """
    return os.getenv("LLM_PROVIDER", "mock").lower()


def rewrite_answer_with_mock(result: str) -> str:
    """
    mock 模式下不调用外部模型，直接返回原始结果。
    这是项目的保底模式。
    """
    return result


def rewrite_answer_with_openai(result: str) -> str:
    """
    预留 OpenAI provider 的回答重写入口。
    当前阶段先不实现真实调用，避免过早绑定单一厂商。
    """
    return result


def rewrite_answer_with_deepseek(result: str) -> str:
    """
    预留 DeepSeek provider 的回答重写入口。
    当前阶段先不实现真实调用，后续可按相同接口补充。
    """
    return result


def rewrite_answer(result: str) -> str:
    """
    根据当前 provider 选择对应的回答重写实现。
    默认使用 mock，确保在未配置真实 API 时系统仍可正常运行。
    """
    provider = get_llm_provider()

    if provider == "openai":
        return rewrite_answer_with_openai(result)
    elif provider == "deepseek":
        return rewrite_answer_with_deepseek(result)
    else:
        return rewrite_answer_with_mock(result)


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
