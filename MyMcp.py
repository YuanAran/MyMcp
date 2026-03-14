# !/usr/bin/env python3
"""
MCP中文统计服务 - 统计纯中文字符数量
"""

import sys
import json


def count_chinese_chars(text: str) -> int:
    """统计纯中文字符数量（Unicode范围：0x4E00-0x9FFF）"""
    return sum(1 for char in text if 0x4E00 <= ord(char) <= 0x9FFF)


def main():
    """MCP服务器主函数"""
    # 设置UTF-8编码
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stdin, 'reconfigure'):
        sys.stdin.reconfigure(encoding='utf-8')

    while True:
        try:
            # 读取请求
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line.strip())
            request_id = request.get("id")
            method = request.get("method")

            # 处理请求
            if method == "tools/list":
                response = {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": {
                        "tools": [{
                            "name": "count_chinese_chars",
                            "description": "统计纯中文字符数量，排除标点、空格、英文字母、数字等",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "text": {
                                        "type": "string",
                                        "description": "需要统计的文本内容"
                                    }
                                },
                                "required": ["text"]
                            }
                        }]
                    }
                }

            elif method == "tools/call":
                tool_name = request.get("params", {}).get("name", "")
                arguments = request.get("params", {}).get("arguments", {})

                if tool_name == "count_chinese_chars":
                    text = arguments.get("text", "")
                    count = count_chinese_chars(text)
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "result": {
                            "content": [{
                                "type": "text",
                                "text": str(count)
                            }]
                        }
                    }
                else:
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "error": {
                            "code": -32601,
                            "message": f"工具 '{tool_name}' 不存在"
                        }
                    }

            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {
                        "code": -32601,
                        "message": f"方法 '{method}' 不存在"
                    }
                }

            # 发送响应
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()

        except json.JSONDecodeError as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"JSON解析错误: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(error_response) + "\n")
            sys.stdout.flush()
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32603,
                    "message": f"内部错误: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(error_response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
