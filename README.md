# MCP中文统计工具（HTTP版）

一个基于MCP（Model Context Protocol）协议的中文字符统计工具，可统计纯中文字符数量，支持 HTTP/Streamable 调用，兼容魔搭网页端。

---

## 功能特性

- ✅ 统计纯中文字符数量  
- ✅ 自动过滤非中文字符（标点、空格、英文、数字等）  
- ✅ 符合 MCP 协议标准  
- ✅ 支持 HTTP/Streamable MCP 调用  

---

## 快速开始

### 安装依赖
```bash
pip install fastapi uvicorn pydantic
启动 HTTP 服务
# 克隆仓库
git clone https://github.com/你的用户名/mcp-chinese-counter.git
cd mcp-chinese-counter

# 启动服务
python MyMcpWrapper.py
暴露公网（开发测试）

如果需要魔搭网页调用，可用 ngrok 暴露端口：

ngrok http 8000

获取生成的公网 URL，例如：

https://capillatus-agnatical-lemuel.ngrok-free.dev
魔搭 MCP 配置（Streamable HTTP）

在魔搭网页端添加 MCP 服务：

{
  "mcpServers": {
    "ChineseCharCounter": {
      "type": "streamable_http",
      "url": "https://capillatus-agnatical-lemuel.ngrok-free.dev/tools/call/count_chinese_chars"
    }
  }
}

⚠️ 注意：url 必须是公网可访问地址，本地 localhost 无法被魔搭网页端访问

工具说明
count_chinese_chars

统计输入文本中的纯中文字符数量。

参数：

text (string, 必需): 需要统计的文本

返回值：

纯中文字符数量（整数），通过 JSON-RPC result.content[0].text 返回

示例：

POST https://capillatus-agnatical-lemuel.ngrok-free.dev/tools/call/count_chinese_chars
Body: {"text": "你好世界！Hello World 123"}

返回：
{
  "jsonrpc": "2.0",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "4"
      }
    ]
  }
}
使用示例（魔搭网页端）

配置 MCP 服务（参考上面的 JSON）

在魔搭聊天中调用：

请使用中文统计工具计算：你好世界！Hello 123

返回结果：

4
技术细节

使用 Unicode 范围 0x4E00-0x9FFF 识别中文字符

符合 MCP JSON-RPC 2.0 标准

HTTP/Streamable MCP 可直接被魔搭网页端调用

许可证

MIT License
