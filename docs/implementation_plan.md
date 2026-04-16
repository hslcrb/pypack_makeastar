# Publishing Plan (v1.1)

This plan outlines the steps to build, release, and publish the `makeastar` package.

## User Review Required

> [!IMPORTANT]
> To proceed with publishing, you must have:
> 1. **PyPI Account**: A registered account on [pypi.org](https://pypi.org/).
> 2. **PyPI API Token**: Generate a token from your PyPI account settings. You will need to provide this when prompted (I will ask for it via a safe method).
> 3. **GitHub Login**: Ensure you are logged in to the GitHub CLI. Run `gh auth login` if you haven't yet.

## Proposed Changes

### Environment Setup
- Create a temporary virtual environment (`.venv_publish`) to install `build` and `twine` without affecting the system environment.
- Install `build` and `twine` inside this venv.

### Build and Release
1. **Build**: Run `python3 -m build` to generate `.whl` and `.tar.gz` artifacts.
2. **PyPI Upload**: Run `python3 -m twine upload dist/*` using your API token.
3. **GitHub Release**: 
   - Tag the current commit as `v1.1`.
   - Use `gh release create v1.1 dist/* --title "v1.1 - Extreme Optimization & New Shapes" --notes "Release notes based on the latest changes."`

## Verification Plan

### Manual Verification
- Verify the package appears on PyPI.
- Verify the release and artifacts appear on GitHub.
