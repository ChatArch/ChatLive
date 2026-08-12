# CLI 树

`ChatLive` 当前是 root-only CLI。这个页面必须从真实 `chatlive --tree` 输出同步，不能手写未来命令。

```text
chatlive  # ChatArch live tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatlive --help` | 已实现 | 显示根命令帮助。 |
| `chatlive --version` | 已实现 | 显示已安装包版本。 |
| `chatlive --tree` | 已实现 | 显示当前真实 CLI 树。 |
| Live tooling 子命令 | 尚未实现 | 未来有真实 live tooling 能力后再加入 CLI。 |

## 更新规则

新增真实命令时，先更新 Click 注册面和测试，再运行 `chatlive --tree` 回填 README 与本页。
