# Network Analog

学生时期的 Python / Pygame 网络路由可视化练习，作为学习记录保留，不承诺持续维护。

## 功能

- 展示 Alice、Bob 两台主机及 A–I 共九个路由器。
- 用 draw line 按钮进入连线模式，依次点击两个路由器添加连接，再点击按钮退出。
- 点击 get table，根据现有连接更新到两台主机的路由表。
- 输入消息后按 F1 从 Alice 向 Bob 发送，显示消息及经过的路径。
- 点击 clean all 重置状态。

这是简化的教学模型，数据包仅包含数据、源和目的标识。

## 运行

创建并激活虚拟环境后，从仓库根目录执行：

```sh
python -m pip install -r requirements.txt
python main.py
```

原仓库环境为 Python 3.7 / Pygame 1.9.6。依赖清单保留原 Pygame 版本用于记录历史环境；尚未验证当前 Python 版本的安装与运行兼容性。图片使用相对路径，需从根目录启动。

## 已知限制

- 节点、布局和连线逻辑为固定配置。
- create_board 会持续向全局 boards_put 追加对象，长时间运行可能导致性能下降。
- link.py 仅为占位文件。

## 整理说明

移除提交中的虚拟环境、字节码缓存和个人 IDE 配置；保留代码、图片和原有提交历史。此次整理未改动模拟逻辑。
