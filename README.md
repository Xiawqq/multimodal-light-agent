# multimodal-light-agent

一个基于 Python 和 OpenCV 的轻量级多模态视频问答原型项目。

## 项目简介

本项目面向视频内容理解场景，构建了一个轻量级 Agent 原型系统。
用户输入自然语言问题后，系统会先进行任务路由，再调用对应的视频处理或规则分析模块，最后生成统一回答。

当前版本以**视频模态**为核心，已实现从“问题输入—任务识别—模块调用—结果返回”的基本闭环。

## 当前功能

- 自然语言问题输入
- 问题路由（video / image / text）
- 视频子任务路由
- 视频总帧数统计
- 视频 FPS 获取
- 视频时长计算
- 基于帧差的运动变化检测
- 基于帧差的明显变化时间定位
- 规则版视频内容分析与回答生成

## 项目结构

- `main.py`：主程序入口，负责整体调度
- `router.py`：问题路由模块
- `video_processor.py`：视频属性处理模块
- `analysis.py`：规则版视频分析模块
- `answer_generator.py`：回答生成模块

## 运行环境

- Python 3.9
- opencv-python

## 安装依赖

```bash
pip install -r requirements.txt