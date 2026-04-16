import os
import router
import video_processor
import analysis
import answer_generator


def main():

    question = input("请输入你的问题：")
    task_type = router.route_question(question)

    print("系统识别的大类任务是：", task_type)

    if task_type == "video":

        video_path = input("请输入视频文件路径：").strip()

        if not os.path.exists(video_path):
            print("系统回答：视频文件不存在，请检查路径是否正确。")
            return

        task_detail = router.route_video_question(question)
        print("系统识别的视频子任务是：", task_detail)

        if task_detail == "duration" or task_detail == "frame_count":
            result = video_processor.process_video(video_path, task_detail)

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
        print("系统回答：暂时还不支持图像处理。")

    else:
        print("系统回答：这是普通文本问题，当前版本暂时不处理。")


if __name__ == "__main__":
    main()