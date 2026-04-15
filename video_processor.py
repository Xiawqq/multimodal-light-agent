import cv2

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

def process_video(video_path: str):
    show_first_frame(video_path)
    return f"已成功读取并展示视频第一帧：{video_path}"