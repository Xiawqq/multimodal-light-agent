import os
import cv2
import router
import answer_generator
from tools import execute_tool, describe_tools

# 测试视频路径     C:\Users\adnim\Desktop\Agent\test.mp4
# 测试图像路径     C:\Users\adnim\Desktop\Agent\test.jpg


# 输出交互展示控制
def handle_modality_task(modality: str, task_detail: str, input_data: str, task_label: str):
    print(f"系统识别的{task_label}子任务是：", task_detail)
    print()

    print("[当前可用工具]")
    print(describe_tools(modality))
    print()

    print("[执行决策]")
    result = execute_tool(modality, task_detail, input_data)
    print()

    print("[工具执行结果]")
    print(result)
    print()

    print("[最终回答]")
    answer = answer_generator.generate_answer(task_detail, result)
    print(answer)


# 检测视频文件是否能正常读取
def is_video_readable(video_path: str) -> bool:     # 规定返回结果为布尔值
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return False
    cap.release()
    return True


def main():

    # 确保有真实问题输入
    question = input("请输入你的问题：").strip()

    if not question:
        print("系统回答：问题不能为空，请重新输入。")
        return

    # 当前版本仅支持开放的一些模态
    task_type = router.route_question(question)

    if task_type not in ["video", "image", "text"]:
        print("系统回答：暂时无法识别你的问题类型。")
        return

    # 确实问题可以被当前的多模态系统处理，开始处理
    print("系统识别的大类任务是：", task_type)

    # # 视频模态
    if task_type == "video":

        video_path = input("请输入视频文件路径：").strip()

        # # # 打开视频出现问题的情况
        if not video_path:
            print("系统回答：视频路径不能为空。")
            return

        if not os.path.exists(video_path):
            print("系统回答：视频文件不存在，请检查路径是否正确。")
            return

        if not is_video_readable(video_path):
            print("系统回答：视频文件无法打开，请确认文件格式是否正确。")
            return

        # # # 分析视频模态子任务，并进入对应的模块
        task_detail = router.route_task_detail(task_type, question)

        handle_modality_task("video", task_detail, video_path, "视频")

    # # 图像模态
    elif task_type == "image":

        image_path = input("请输入图片文件路径：").strip()

        # # # 打开视频出现问题的情况
        if not image_path:
            print("系统回答：图片路径不能为空。")
            return

        if not os.path.exists(image_path):
            print("系统回答：图片文件不存在，请检查路径是否正确。")
            return

        # # # 分析视频模态子任务，并进入对应的模块
        task_detail = router.route_task_detail(task_type, question)

        handle_modality_task("image", task_detail, image_path, "图像")


    # # 文本模态
    else:
        text_input = input("请输入要处理的文本内容：").strip()

        if not text_input:
            print("系统回答：文本内容不能为空。")
            return

        task_detail = router.route_task_detail(task_type, question)

        handle_modality_task("text", task_detail, text_input, "文本")


if __name__ == "__main__":
    main()
