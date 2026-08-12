# CLI Tree

`ChatLive` is currently a root-only CLI. This page must stay synchronized from the real `chatlive --tree` output and must not invent future commands.

```text
chatlive  # ChatArch live tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatlive --help` | Implemented | Shows root command help. |
| `chatlive --version` | Implemented | Shows the installed package version. |
| `chatlive --tree` | Implemented | Shows the current real CLI tree. |
| Live tooling subcommands | Not implemented | Add them only after real live tooling capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatlive --tree` to refresh README and this page.
