import os
import cv2
import router
import video_processor
import analysis
import answer_generator


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
        task_detail = router.route_video_question(question)
        print("系统识别的视频子任务是：", task_detail)

        if task_detail == "duration":
            result = video_processor.get_video_duration(video_path)

        elif task_detail == "frame_count":
            result = video_processor.get_video_frame_count(video_path)

        elif task_detail == "motion":
            result = analysis.analyze_motion(video_path)

        elif task_detail == "change_time":
            result = analysis.analyze_change_time(video_path)

        elif task_detail == "summary":
            result = analysis.analyze_summary(video_path)

        else:
            result = analysis.analyze_video_content(video_path)

        answer = answer_generator.generate_answer(task_detail, result)
        print(answer)

    elif task_type == "image":
        print("系统回答：当前版本暂时还不支持图像处理。")

    else:
        print("系统回答：当前版本暂时还不支持普通文本问题处理。")


if __name__ == "__main__":
    main()