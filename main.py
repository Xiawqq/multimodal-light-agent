import router
import video_processor
import analysis
import answer_generator


def main():

    question = input("请输入你的问题：")
    task_type = router.route_question(question)

    print("系统识别的大类任务是：", task_type)

    if task_type == "video":

        task_detail = router.route_video_question(question)
        print("系统识别的视频子任务是：", task_detail)

        if task_detail == "duration" or task_detail == "frame_count":
            result = video_processor.process_video("test.mp4", task_detail)

        elif task_detail == "motion":
            result = analysis.analyze_motion("test.mp4")

        elif task_detail == "change_time":
            result = analysis.analyze_change_time("test.mp4")

        elif task_detail == "summary":
            result = analysis.analyze_summary("test.mp4")

        else:
            result = analysis.analyze_video_content("test.mp4")

        answer = answer_generator.generate_answer(task_detail, result)
        print(answer)

    elif task_type == "image":
        print("系统回答：暂时还不支持图像处理。")

    else:
        print("系统回答：这是普通文本问题，当前版本暂时不处理。")


if __name__ == "__main__":
    main()