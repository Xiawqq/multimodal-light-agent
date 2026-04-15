"""

视频模态处理

"""


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


# 获取视频 FPS
def get_video_fps(video_path: str):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return -1

    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    return fps


# 计算视频总帧数 + 展示第一帧 + 交互说明
def process_video(video_path: str, task_detail: str):

    frame_count = count_frames(video_path)
    fps = get_video_fps(video_path)

    if frame_count == -1 or fps == -1 or fps == 0:
        return "视频打开失败或无法获取视频信息"

    duration = frame_count / fps

    if task_detail == "duration":
        return f"视频时长约为：{duration:.2f} 秒"

    elif task_detail == "frame_count":
        return f"视频总帧数为：{frame_count}"

    else:
        show_first_frame(video_path)
        return f"已成功读取并展示视频第一帧，视频总帧数为：{frame_count}，视频时长约为：{duration:.2f} 秒"