# IFREAD's Web - 个人网站

这是IFREAD的个人网站，一个现代化的多功能网站，包含治愈花园、效率工具等特色功能模块。

## 🌟 项目概述

这是一个集个人展示、工具应用、放松娱乐于一体的现代化个人网站，采用响应式设计，具有优雅的动画效果和用户体验。

## 📁 项目结构

```
├── index.html              # 主页 - 网站入口
├── healing-garden.html     # 治愈花园 - 放松休闲页面
├── efficiency.html         # 效率工具 - 实用工具集合
├── developer.html          # 开发者信息页面
├── styles/                 # 样式文件目录
│   ├── main.css           # 主要样式文件
│   ├── healing-garden.css # 治愈花园专用样式
│   ├── efficiency.css     # 效率工具专用样式
│   ├── welcome-animation.css # 入场动画样式
│   ├── hero-animation.css # 主页动画样式
│   ├── image-transition.css # 图片过渡效果
│   └── healing-invitation.css # 治愈花园邀请区样式
├── scripts/               # JavaScript文件目录
│   ├── main.js           # 主要交互脚本
│   ├── healing-garden.js # 治愈花园功能脚本
│   └── efficiency.js     # 效率工具功能脚本
├── images/               # 图片资源目录
│   ├── favicon.png.png   # 网站图标
│   ├── ifread.jpg        # 开发者头像
│   ├── plant-*.svg       # 植物生长动画素材
│   └── sunset/           # 日落图片集合
├── audio/                # 音频资源目录
│   ├── calm-waters.mp3   # 平静水声
│   ├── gentle-breeze.mp3 # 轻柔微风
│   └── peaceful-morning.mp3 # 宁静晨光
└── README.md             # 项目说明文档
```

## ✨ 功能特点

### 🏠 主页功能
- 优雅的入场动画效果（"终于等到你了"）
- 响应式导航菜单设计
- 治愈花园邀请区域，引导用户体验放松功能
- 现代化的视觉设计和交互效果

### 🌸 治愈花园
- **植物养成系统**：虚拟植物从种子到成熟的生长动画
- **自然音效播放**：多种舒缓的自然声音（水声、风声、晨光）
- **日落图片轮播**：精美的日落景色图片展示
- **放松氛围营造**：专为减压和放松设计的交互体验

### ⚡ 效率工具
- **实时翻页时钟**：具有翻页动画效果的数字时钟
- **全屏显示功能**：支持时钟全屏显示
- **专注时光体验**：帮助用户提升工作效率

### 👨‍💻 开发者页面
- 开发者个人信息展示
- 社交媒体链接（GitHub、博客等）
- 项目开发背景介绍

### 🎨 设计特色
- 完全响应式设计，适配各种屏幕尺寸
- 流畅的页面过渡和动画效果
- 现代化的UI设计风格
- 优秀的用户体验和交互设计

## 🚀 使用方法

### 直接访问
直接在浏览器中打开 `index.html` 文件即可查看网站

### 本地服务器运行
```bash
# 使用Python
python -m http.server 8000

# 使用Node.js
npx serve .

# 使用PHP
php -S localhost:8000
```

然后在浏览器中访问 `http://localhost:8000`

## 🛠️ 自定义修改

### 内容修改
- 修改各HTML文件中的文本内容和结构
- 更换 `images/` 目录中的图片资源
- 替换 `audio/` 目录中的音频文件

### 样式调整
- `styles/main.css` - 调整全局样式、颜色主题、字体
- `styles/healing-garden.css` - 修改治愈花园的视觉效果
- `styles/efficiency.css` - 调整效率工具的界面样式

### 功能扩展
- `scripts/` 目录中的JavaScript文件可以添加新的交互功能
- 可以在治愈花园中添加更多放松功能
- 在效率工具中集成更多实用工具

## 📱 响应式支持

网站完全支持响应式设计，在以下设备上都有良好的显示效果：
- 桌面电脑（1200px+）
- 平板设备（768px - 1199px）
- 手机设备（< 768px）

## 🔧 技术栈

- **前端框架**：原生HTML5 + CSS3 + JavaScript
- **图标库**：Font Awesome 6.0
- **动画效果**：CSS3 Animations & Transitions
- **响应式**：CSS Media Queries
- **音频处理**：HTML5 Audio API

## 📝 注意事项

- 网站使用了Font Awesome图标库，需要保持互联网连接才能正常显示图标
- 音频文件需要用户交互后才能播放（浏览器安全策略）
- 建议使用现代浏览器以获得最佳体验
- 所有代码均为原创，遵循开源协议

## 🎯 未来计划

- [ ] 添加更多治愈花园功能（冥想指导、呼吸练习等）
- [ ] 扩展效率工具集合（番茄钟、待办清单等）
- [ ] 集成教育大模型功能
- [ ] 优化移动端体验
- [ ] 添加用户个性化设置

## 👤 关于开发者

**IFREAD** - 全栈开发者  
- 博客：[IFREAD的博客](https://www.cnblogs.com/IFREAD-LI/)
- GitHub：[IFREAD](https://github.com)

---

*让技术服务生活，让代码创造美好* ✨