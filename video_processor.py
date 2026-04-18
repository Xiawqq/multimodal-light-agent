"""

视频属性处理

"""


import cv2
from utils import open_video


# 播放完整视频
def play_video(video_path):

    cap = open_video(video_path)

    if cap is None:
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

    cap = open_video(video_path)

    if cap is None:
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
def get_video_frame_count(video_path: str):

    cap = open_video(video_path)

    if cap is None:     # 视频能不能打开
        return "视频打开失败或无法获取视频信息"

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_count <= 0:    # 视频打开了有没有内容
        return "视频打开失败或无法获取视频信息"

    cap.release()
    return f"视频总帧数为：{frame_count}"


# 获取视频 FPS
def get_video_fps(video_path: str):
    cap = open_video(video_path)

    if cap is None:     # 视频能不能打开
        return -1

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:    # 视频打开了有没有内容
        return -1

    cap.release()
    return f"视频总帧数为：{fps}"


# 计算视频时长
def get_video_duration(video_path: str):

    cap = open_video(video_path)

    if cap is None:
        return "视频打开失败或无法获取视频信息"

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if frame_count <= 0 or fps <= 0:
        return "视频打开失败或无法获取视频信息"

    duration = frame_count / fps
    cap.release()
    return f"视频时长约为：{duration:.2f} 秒"