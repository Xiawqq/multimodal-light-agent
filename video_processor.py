"""

视频属性处理

"""


import cv2
from utils import open_video


# 计算视频总帧数
def get_video_frame_count(video_path: str):

    cap = open_video(video_path)

    if cap is None:     # 视频能不能打开
        return "视频打开失败或无法获取视频信息"

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_count <= 0:    # 视频打开了有没有内容
        cap.release()
        return "视频打开失败或无法获取视频信息"

    cap.release()
    return f"视频总帧数为：{frame_count}"


# 获取视频 FPS
def get_video_fps(video_path: str):
    cap = open_video(video_path)

    if cap is None:     # 视频能不能打开
        return "视频打开失败或无法获取视频帧率信息"

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:    # 视频打开了有没有内容
        cap.release()
        return "视频打开失败或无法获取视频帧率信息"

    cap.release()
    return f"视频帧率约为：{fps:.2f} FPS"


# 计算视频时长
def get_video_duration(video_path: str):

    cap = open_video(video_path)

    if cap is None:
        return "视频打开失败或无法获取视频信息"

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if frame_count <= 0 or fps <= 0:
        cap.release()
        return "视频打开失败或无法获取视频信息"

    duration = frame_count / fps
    cap.release()
    return f"视频时长约为：{duration:.2f} 秒"
