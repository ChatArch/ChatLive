<div align="center">
    <a href="https://pypi.python.org/pypi/ChatLive">
        <img src="https://img.shields.io/pypi/v/ChatLive.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatLive/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatLive/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatLive/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatLive

ChatLive is the ChatArch live tooling package entrypoint. The package currently keeps a minimal root-only CLI so the live tooling shell remains installable, discoverable, and releasable; real live subcommands are not exposed yet.

## Quick Start

```bash
pip install ChatLive
chatlive --help
chatlive --version
chatlive --tree
```

## Current CLI Tree

```text
chatlive  # ChatArch live tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## CLI Boundary

- The current CLI only exposes root options and has no business subcommands.
- `--tree` is generated from the real Click command registration and is used to align README, docs, and tests.
- When real live tooling commands are added later, update the Click registration first and then sync docs from the real `chatlive --tree` output.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by MkDocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
