# MCP 中文字符统计服务

## 功能
统计传入文本中的中文字符数量（不包含标点、空格、英文、数字等），并返回结果。  
兼容魔搭 JSON-RPC 调用规范，适合 Streamable HTTP 部署。

## 接口说明

### 查询工具列表
**GET** `/tools/list`  
返回 MCP 提供的工具信息，示例：

```json
{
  "jsonrpc": "2.0",
  "result": {
    "tools": [
      {
        "name": "count_chinese_chars",
        "description": "统计纯中文字符数量",
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
      }
    ]
  }
}
调用中文统计工具

POST /tools/call/count_chinese_chars
请求示例（JSON-RPC 格式）：

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "count_chinese_chars",
    "arguments": {
      "text": "这里是一段测试文字"
    }
  }
}

返回示例：

{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "8"
      }
    ]
  }
}

"text" 字段即返回的中文字符数量。

注意事项

支持 POST、DELETE、OPTIONS 请求，兼容魔搭部署检测。

使用 Streamable HTTP 模式部署时，请在 JSON 配置中填写完整 URL，例如：

https://你的域名/tools/call/count_chinese_chars

返回内容遵循 JSON-RPC 规范，方便 DeepSeek 或其他模型调用。

适合统计纯中文字符，不包含标点、空格、英文和数字。
许可证

MIT License
