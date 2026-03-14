# MCP中文统计工具

一个基于MCP（Model Context Protocol）协议的中文字符统计工具，可统计纯中文字符数量。

## 功能特性

- ✅ 统计纯中文字符数量
- ✅ 自动过滤非中文字符（标点、空格、英文、数字等）
- ✅ 符合MCP协议标准
- ✅ 支持STDIO通信方式

## 快速开始

### 安装依赖
无需额外依赖，只需Python 3.6+。

### 本地运行测试
```bash
# 克隆仓库
git clone https://github.com/你的用户名/mcp-chinese-counter.git
cd mcp-chinese-counter

# 运行MCP服务
python server.py
```

## MCP配置（魔塔社区专用）

### STDIO配置
在魔塔社区的MCP设置中使用以下配置：

```json
{
  "mcpServers": {
    "chinese-counter": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

### 环境变量（可选）
```json
{
  "mcpServers": {
    "chinese-counter": {
      "command": "python",
      "args": ["server.py"],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

## 工具说明

### `count_chinese_chars`
统计输入文本中的纯中文字符数量。

**参数：**
- `text` (string, 必需): 需要统计的文本

**返回值：**
- 纯中文字符数量（整数）

**示例：**
```json
{
  "text": "你好世界！Hello World 123"
}
// 返回: 4
```

## 使用示例

1. **在魔塔社区配置MCP服务**
2. **在聊天中调用：**
   ```
   请使用中文统计工具计算：你好世界！Hello 123
   ```
3. **返回结果：** `4`

## 技术细节

- 使用Unicode范围 `0x4E00-0x9FFF` 识别中文字符
- 符合MCP协议JSON-RPC 2.0标准
- 通过STDIO进行进程间通信

## 许可证

MIT License
