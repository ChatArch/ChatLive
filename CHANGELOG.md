# Changelog

## 0.1.2 - 2026-08-22

### Added
- Added `chatlive --tree-brief`, which renders the same registered command surface without parameter signatures.
- Added full/brief tree contract tests and installed console-script CI readbacks.

### Changed
- Replaced the package-local tree renderer with ChatStyle `add_tree_option()` and required `chatstyle>=0.2.0,<0.3.0`.
- Made the public `chatlive` root name explicit and synchronized bilingual CLI tree documentation with runtime output.
- Bounded Click and MkDocs Material to the supported compatibility ranges.

## 0.1.1 - 2026-08-12

### Added
- Added real root-only `chatlive --tree` generated from the Click command surface.
- Added bilingual MkDocs home and CLI tree pages.
- Added CLI and workflow/docs contract tests.

### Changed
- Reduced runtime dependencies to `click>=8.0` because no ChatStyle/ChatEnv command surface remains.
- Aligned documentation URL to `https://arch.gh.wzhecnu.cn/ChatLive/`.
- Hardened CI, Preview Docs, Deploy Docs, and tag-only OIDC publish workflows.

## 0.1.0 - 2026-07-05

### Added
- First tag-driven release through GitHub Actions and PyPI Trusted Publisher.

## 0.0.1 - 2026-07-05

### Added
- Initial project baseline for PyPI registration.
