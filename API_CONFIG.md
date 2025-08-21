# SiliconFlow API 配置指南

## 🚀 快速开始

本项目已集成 SiliconFlow 的真实 AI 对话功能，让治愈花园的 AI 助手能够提供更智能、更贴心的回复。

## 📋 配置步骤

### 1. 获取 API 密钥

1. 访问 [SiliconFlow 官网](https://cloud.siliconflow.cn)
2. 注册账号并完成认证
3. 在控制台中创建 API 密钥
4. 复制您的 API 密钥

### 2. 配置项目

打开 `scripts/healing-garden.js` 文件，找到以下行：

```javascript
const SILICONFLOW_API_KEY = 'YOUR_API_KEY_HERE'; // 请替换为您的API密钥
```

将 `YOUR_API_KEY_HERE` 替换为您的真实 API 密钥：

```javascript
const SILICONFLOW_API_KEY = 'sk-your-actual-api-key-here';
```

### 3. 模型选择

当前使用的是 `deepseek-chat` 模型，您也可以根据需要修改为其他支持的模型：

```javascript
const AI_MODEL = 'deepseek-chat'; // 可选择其他模型
```

支持的模型包括：
- `deepseek-chat` - DeepSeek 对话模型
- `glm-4-9b-chat` - GLM-4 模型
- `qwen-plus` - 通义千问模型
- 更多模型请查看 SiliconFlow 官方文档

## 🌟 功能特色

### AI 助手特点
- **智能理解**：基于上下文的智能对话
- **情感支持**：专门优化的治愈系回复
- **记忆功能**：保持对话连贯性（最近10轮对话）
- **备用机制**：API 失败时自动切换到本地回复

### 系统提示词
当前 AI 助手被设定为：
- 温柔、耐心、善解人意的治愈系助手
- 名字叫"小花🌸"
- 专注于提供情感支持和心理慰藉
- 回复简洁温暖，不超过100字

## 🔧 高级配置

### 调整 AI 参数

在 `callSiliconFlowAPI` 函数中，您可以调整以下参数：

```javascript
body: JSON.stringify({
    model: AI_MODEL,
    messages: messages,
    temperature: 0.7,    // 创造性程度 (0-1)
    max_tokens: 200,     // 最大回复长度
    stream: false        // 是否流式输出
})
```

### 自定义系统提示词

修改 `SYSTEM_PROMPT` 常量来调整 AI 助手的性格和回复风格：

```javascript
const SYSTEM_PROMPT = `你是一个温暖治愈的AI助手，名叫小花🌸...
// 在这里自定义您的提示词
`;
```

## 💰 费用说明

- SiliconFlow 提供免费额度供新用户体验
- 企业认证用户可获得 500 元赠金
- 学生认证用户可获得 50 元赠金
- 按实际使用量计费，费用透明

## 🛡️ 安全注意事项

1. **保护 API 密钥**：不要将 API 密钥提交到公共代码仓库
2. **使用环境变量**：生产环境建议使用环境变量存储密钥
3. **监控使用量**：定期检查 API 使用情况，避免意外费用

## 🔄 备用方案

如果 API 调用失败，系统会自动：
1. 显示错误提示
2. 切换到本地预设回复
3. 保持用户体验的连续性

## 📞 技术支持

如果遇到配置问题：
1. 查看浏览器控制台的错误信息
2. 确认 API 密钥格式正确
3. 检查网络连接状态
4. 参考 SiliconFlow 官方文档

---

配置完成后，重新加载页面即可体验真实的 AI 对话功能！🎉