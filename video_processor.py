import cv2


# 播放完整视频
def play_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("视频打开失败")
        return

    while 1:
        ret,frame=cap.read()

        if ret==False:
            print("视频播放结束")
            break

        cv2.imshow("frame",frame)

        if cv2.waitKey(30)==27:
            print("用户手动退出播放")
            break

    cap.release()
    cv2.destroyAllWindows()


# 展示视频第一帧
def show_first_frame(video_path):
    cap=cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("视频打开失败")
        return

    ret, frame = cap.read()

    if ret:
        cv2.imshow("first frame", frame)
        cv2.waitKey(0)
    else:
        print("无法读取第一帧")

    cap.release()
    cv2.destroyAllWindows()


# 计算视频总帧数
def count_frames(video_path: str):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return -1

    frame_count = 0

    while 1:
        ret, frame = cap.read()
        if ret == False :
            break
        else:
            frame_count += 1

    cap.release()
    return frame_count


# 计算视频总帧数 + 展示第一帧 + 交互说明
def process_video(video_path: str):
    frame_count = count_frames(video_path)

    if frame_count == -1:
        return "视频打开失败"
    else:
        show_first_frame(video_path)

    return f"已成功读取并展示视频第一帧，视频总帧数为：{frame_count}"
