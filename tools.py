import video_processor
import analysis
import image_processor
import text_processor

# 现存的视频工具库
VIDEO_TOOLS = {
    "duration": {
        "name": "get_video_duration",
        "description": "获取视频总时长",
        "modality": "video",
        "input_type": "video_path",
        "output_type": "text",
        "keywords": ["时长", "多久", "duration"],
        "example_question": "这个视频有多长？",
        "func": video_processor.get_video_duration,
    },
    "frame_count": {
        "name": "get_video_frame_count",
        "description": "获取视频总帧数",
        "modality": "video",
        "input_type": "video_path",
        "output_type": "text",
        "keywords": ["帧数", "总帧数", "多少帧"],
        "example_question": "这个视频一共有多少帧？",
        "func": video_processor.get_video_frame_count,
    },
    "fps": {
        "name": "get_video_fps",
        "description": "获取视频帧率",
        "modality": "video",
        "input_type": "video_path",
        "output_type": "text",
        "keywords": ["帧率", "fps", "每秒多少帧"],
        "example_question": "这个视频的帧率是多少？",
        "func": video_processor.get_video_fps,
    },
    "motion": {
        "name": "analyze_motion",
        "description": "检测视频中是否存在明显运动",
        "modality": "video",
        "input_type": "video_path",
        "output_type": "text",
        "keywords": ["运动", "活动", "明显运动"],
        "example_question": "这个视频里有明显运动吗？",
        "func": analysis.analyze_motion,
    },
    "change_time": {
        "name": "analyze_change_time",
        "description": "定位视频中变化最明显的时间点",
        "modality": "video",
        "input_type": "video_path",
        "output_type": "text",
        "keywords": ["变化时间", "什么时候变化", "变化最明显"],
        "example_question": "这个视频什么时候变化最明显？",
        "func": analysis.analyze_change_time,
    },
    "summary": {
        "name": "analyze_summary",
        "description": "生成视频内容概括",
        "modality": "video",
        "input_type": "video_path",
        "output_type": "text",
        "keywords": ["概括", "总结", "主要讲了什么"],
        "example_question": "概括一下这个视频内容。",
        "func": analysis.analyze_summary,
    },
    "content": {
        "name": "analyze_video_content",
        "description": "分析视频主要内容",
        "modality": "video",
        "input_type": "video_path",
        "output_type": "text",
        "keywords": ["内容", "主要内容", "发生了什么"],
        "example_question": "这个视频里发生了什么？",
        "func": analysis.analyze_video_content,
    },
}


# 现存的图像工具库
IMAGE_TOOLS = {
    "size": {
        "name": "get_image_size",
        "description": "获取图片宽度和高度",
        "modality": "image",
        "input_type": "image_path",
        "output_type": "text",
        "keywords": ["尺寸", "大小", "宽高"],
        "example_question": "这张图片的尺寸是多少？",
        "func": image_processor.get_image_size,
    }
}


# 现存的文本工具库
TEXT_TOOLS = {
    "length": {
        "name": "get_text_length",
        "description": "统计文本字符长度",
        "modality": "text",
        "input_type": "text",
        "output_type": "text",
        "keywords": ["字数", "长度", "字符数"],
        "example_question": "这段文本有多少个字符？",
        "func": text_processor.get_text_length,
    }
}


# 多模态工具库合集
ALL_TOOLS = {
    "video": VIDEO_TOOLS,
    "image": IMAGE_TOOLS,
    "text": TEXT_TOOLS,
}


# 处理工具选择
def execute_tool(modality: str, task_detail: str, input_data: str):
    modality_tools = ALL_TOOLS.get(modality)

    if modality_tools is None:
        return "暂时不支持该模态。"

    tool_info = modality_tools.get(task_detail)

    if tool_info is None:
        return f"暂时无法处理该{modality}任务。"

    print("系统选择的工具是：", tool_info["name"])
    tool_func = tool_info["func"]
    return tool_func(input_data)