# MyMcpWrapper.py
"""
HTTP 包装版 MCP 中文统计服务
兼容魔搭 JSON-RPC 请求，同时支持魔搭部署检测
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(title="MCP中文统计HTTP服务")


def count_chinese_chars(text: str) -> int:
    """统计纯中文字符数量"""
    return sum(1 for char in text if 0x4E00 <= ord(char) <= 0x9FFF)


@app.api_route("/tools/call/count_chinese_chars", methods=["POST", "DELETE", "OPTIONS"])
async def call_count_chinese_chars(request: Request):
    if request.method == "POST":
        try:
            data = await request.json()
            request_id = data.get("id")
            method = data.get("method")

            if method != "tools/call":
                return JSONResponse(
                    content={
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "error": {"code": -32601, "message": f"方法 '{method}' 不存在"}
                    }
                )

            params = data.get("params", {})
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})

            if tool_name != "count_chinese_chars":
                return JSONResponse(
                    content={
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "error": {"code": -32601, "message": f"工具 '{tool_name}' 不存在"}
                    }
                )

            text = arguments.get("text", "")
            count = count_chinese_chars(text)

            return JSONResponse(
                content={
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": {
                        "content": [{"type": "text", "text": str(count)}]
                    }
                }
            )

        except Exception as e:
            return JSONResponse(
                content={
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32603, "message": f"内部错误: {str(e)}"}
                }
            )
    else:
        # DELETE / OPTIONS 请求返回空响应，兼容魔搭部署检测
        return JSONResponse(content={"status": "ok"})


@app.get("/tools/list")
async def list_tools():
    return JSONResponse(
        content={
            "jsonrpc": "2.0",
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
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("MyMcpWrapper:app", host="0.0.0.0", port=8000, reload=True)
