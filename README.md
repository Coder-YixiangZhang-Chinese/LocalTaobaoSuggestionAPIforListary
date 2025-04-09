# LocalTaobaoSuggestionAPIforListary

🌐 语言: [简体中文](README.md) | [English](README.en-US.md)

一个轻量级的本地 HTTP 接口服务，模拟淘宝搜索建议的响应格式，适用于 [Listary](https://www.listary.com/) 。  
支持脱机运行（使用预设数据时），接口稳定，开箱即用，让你的搜索体验更加智能与高效。

---

## ✨ 功能特点

- 🛍️ 本地模拟淘宝搜索关键词联想（支持预设或爬取数据）
- ⚙️ 兼容 Listary 的建议词接口标准
- 📡 提供 HTTP API 接口，可静默后台运行
- 📦 可打包为 `.exe`，开机自启无打扰
- 🔒 内置端口冲突检测，防止多实例运行

---

## 📦 安装运行

### 方式一：使用源码运行

1. 安装 Python（推荐 3.8+）  
2. 安装依赖：
```bash
pip install requests flask
```
3. 运行源码：
```bash
python taobaoSearchAPI.py
```
### 方式二：直接使用预打包文件

下载(Release)[]中的`.exe`文件，开启后即可打开静默运行的本地服务端。（默认IP:端口127.0.0.1:60000）

### 方式三：自行打包本地服务端

下载源码后使用指令：
```bash
pyinstaller --onefile --noconsole taobao_suggest_api.py
```
将源码打包成`.exe`（后台静默运行），可以进一步自行添加到开机自启中

#### 默认监听地址为：
```bash
http://localhost:60000/suggest?q=搜索词
```

---

## 🔗Listary配置

1. 启动本地服务端（.py 或 .exe 均可）
2. 打开 Listary 选项面板 → 网络搜索 → 添加新搜索项
3. 关键配置：
   - 关键字：@tb或自定义
   - 标题：淘宝或自定义
   - 搜索URL：```https://s.taobao.com/search?q={query}```
   - 搜索提示改为Custom：```http://127.0.0.1:60000/suggest?q={query}```

⚠️如果你自定义端口或重新打包服务端，请同步修改 Listary 的搜索建议地址。

此外，程序内置端口检测机制以避免多实例冲突，如需修改监听端口，请同时修改源码中的监听端口号。

图解：

![image](https://github.com/user-attachments/assets/735ea0d4-98c7-4c0f-832d-ef395618ed9a)

![image](https://github.com/user-attachments/assets/c1ff7e30-491a-406c-ad8e-86efd77c9823)

![image](https://github.com/user-attachments/assets/794acb5c-35c6-4967-8d9a-70d11bbf421f)

---

## 📜 开源许可

本项目采用 CC BY-NC 4.0 开源协议，欢迎自由使用、分发与改进。

---

## 🙌 开发者交流与贡献

- 欢迎提交 PR、Issue 或建议
- 如果你希望扩展为 Flow Launcher 插件版本，也欢迎联系我一同开发！
