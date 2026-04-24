"""
LLM 接口层

当前阶段先不直接接入真实大模型 API，
而是预留统一的 AI 能力入口，便于后续逐步替换规则逻辑。
"""


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


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


# DeepSeek provider 的回答重写入口
def rewrite_answer_with_deepseek(result: str) -> str:
    """
    使用 DeepSeek 官方 API 对工具执行结果进行自然语言重写。
    如果未配置 API Key 或调用失败，则回退到原始结果。
    """
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return result

    # # 根据 DeepSeek 官方文档构造 API 请求，进行回答重写
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
    )
    # # 构造提示语，引导模型将工具结果改写成简洁、自然、准确的中文回答
    try:
        response = client.chat.completions.create(
            model=model,

            # # 这里的提示语可以根据实际情况调整，以获得更符合预期的回答重写效果
            messages=[
                # # # system 角色的提示语非常重要，它直接影响模型对重写任务的理解和执行效果
                {
                    "role": "system",
                    "content": "请把给定的工具执行结果改写成简洁、自然、准确的中文回答，不要添加原结果中没有的新事实。",
                },
                # # # user 角色的内容就是工具执行的原始结果，模型需要基于这个内容进行重写
                {
                    "role": "user",
                    "content": result,
                },
            ],
            # # 适当调整 temperature 参数，可以让模型生成的回答更有创造性或更保守，具体数值可以根据实际需求进行微调
            temperature=0.3,
        )

        content = response.choices[0].message.content

        return content.strip() if content else result
    
    # 捕获可能的异常，例如网络错误、API 错误等，确保在发生问题时系统仍能正常运行，并返回原始结果
    except Exception:
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
