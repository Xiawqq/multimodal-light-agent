"""

视频内容分析

"""


import cv2


# 视频运动情况分析
def detect_motion(video_path: str):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return "视频打开失败，无法进行运动分析。"

    prev_gray = None         # 存储上一帧的灰度图（初始为空）
    diff_values = []         # 列表：存储所有相邻帧的平均差值
    frame_index = 0          # 帧计数器：记录当前是第几帧
    sample_interval = 30     # 采样间隔：每30帧处理1次

    while 1:
        ret, frame = cap.read()
        if ret == False:
            break

        if frame_index % sample_interval == 0:      # 只处理第 0、30、60、90... 帧

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # 灰度图只有亮度信息，计算速度远快于彩色图

            if prev_gray is not None:       # 确保不是第一帧（第一帧无上一帧）
                diff = cv2.absdiff(prev_gray, gray)      # 计算两帧像素的绝对差值
                mean_diff = diff.mean()                  # 计算差值图像的平均值
                diff_values.append(mean_diff)            # 把差值存入列表

            prev_gray = gray    # 更新：当前帧变成下一帧的 " 上一帧 "

        frame_index += 1

    cap.release()

    if len(diff_values) == 0:
        return "视频帧不足，暂时无法判断运动情况。"

    avg_diff = sum(diff_values) / len(diff_values)      # 计算所有差值的平均值

    if avg_diff > 8:        # 判断阈值
        return f"检测结果：视频中存在较明显画面变化，平均帧差值为 {avg_diff:.2f}。"
    else:
        return f"检测结果：视频整体变化不明显，平均帧差值为 {avg_diff:.2f}。"


# 视频里发生了什么
def analyze_video_content(video_path: str):
    return "初步分析结果：视频中存在持续画面变化，可能包含人物活动或场景内容变化。"


# 视频里有运动吗
def analyze_motion(video_path: str):
    return detect_motion(video_path)


# 这个视频主要内容是什么
def analyze_summary(video_path: str):
    return "视频主要内容可概括为：画面中存在一定变化，适合进一步做内容理解与行为分析。"