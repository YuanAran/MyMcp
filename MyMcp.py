#!/usr/bin/env python3
"""
MCP中文统计服务 - 统计纯中文字符数量
兼容魔搭 Python MCP 托管模式
"""

import sys
import json
from modelscope_mcp import MCP  # 魔搭官方 MCP 框架

# 创建 MCP 实例
mcp_instance = MCP()

# 注册工具
@mcp_instance.tool
def count_chinese_chars(text: str) -> int:
    """
    统计纯中文字符数量（Unicode范围：0x4E00-0x9FFF）
    排除标点、空格、英文字母、数字等
    """
    return sum(1 for char in text if 0x4E00 <= ord(char) <= 0x9FFF)

# 设置 UTF-8 编码（可选，保证中文输出）
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stdin, 'reconfigure'):
    sys.stdin.reconfigure(encoding='utf-8')

# 启动 MCP
if __name__ == "__main__":
    mcp_instance.run(transport='stdio')
