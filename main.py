import router
import video_processor


def main():
    question = input("请输入你的问题：")
    task_type = router.route_question(question)

    print("识别到的任务类型是：", task_type)

    if task_type == "video":

        task_detail = router.route_video_question(question)
        print("识别到的视频问题类型是：", task_detail)

        if task_detail == "summary":
            print("开始处理视频并展示第一帧...")
        result = video_processor.process_video("test.mp4", task_detail)
        print("处理结果：", result)

    elif task_type == "image":
        print("暂时还不支持图像处理")

    else:
        print("这是普通文本问题，暂时不处理")


if __name__ == "__main__":
    main()