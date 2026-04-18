'''
    相关模态对应的文件打开模块
'''

import cv2

# 视频模态
def open_video(video_path: str):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None
    return cap