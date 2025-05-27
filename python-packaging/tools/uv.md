# uv

uv: An extremely fast Python package and project manager, written in Rust.

## Source

- Website: https://docs.astral.sh/uv/
- GitHub Repository: https://github.com/astral-sh/uv

### Usage

Installing `uv`:
```shell
curl -fsSL https://astral.sh/uv/install.sh | sh
```

Enable shell autocompletion for `uv`:
```shell
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
```

Unistalling `uv`:
```shell
rm ~/.cargo/bin/uv ~/.cargo/bin/uvx
```

Update `uv` to the latest version:
```shell
uv self update
```

### Python

Install a specific Python version:
```shell
uv python install 3.12
```

### Venv

Create a virtual environment without project:
```shell
uv venv --no-project venv
```

Activate virtual environment:
```shell
source venv/bin/activate
```

### Pip

Make sure you have a virtual environment created to use `uv pip` following this guide, `uv` also works with `--system`, but this is not addressed in this guide.

List packages installed in an environment:
```shell
uv pip list
```

Install packages into an environment:
```shell
uv pip install <package-name>
```

Uninstall packages from an environment:
```shell
uv pip uninstall <package-name>
```

### Cache

Clear the cache, removing all entries or those linked to specific packages:
```shell
uv cache clean
```

Prune all unreachable objects from the cache:
```shell
uv cache prune
```

Show the cache directory:
```shell
uv cache dir
```

> [!NOTE]
> See more about uv cache in [uv cache](https://docs.astral.sh/uv/concepts/cache/#cache-directory)

## Related links

- [uv: Unified Python packaging from Astral](https://astral.sh/blog/uv-unified-python-packaging)
- [uv: Unified Python packaging from Simon Willison](https://simonwillison.net/2024/Aug/20/uv-unified-python-packaging/)
- [Python: my new uv setup for development](https://adamj.eu/tech/2024/09/18/python-uv-development-setup/)
- [Switching from pyenv to uv](https://bluesock.org/~willkg/blog/dev/switch_pyenv_to_uv.html)
- [Docker images using uv's python](https://mkennedy.codes/posts/python-docker-images-using-uv-s-new-python-features/)
- [Production-ready Docker Containers with uv](https://hynek.me/articles/docker-uv/)
- [Switching from virtualenvwrapper to direnv, Starship, and uv](https://treyhunner.com/2024/10/switching-from-virtualenvwrapper-to-direnv-starship-and-uv/)
- [A comprehensive guide to python project management and packaging concepts illustrated with uv part 1](https://reinforcedknowledge.com/a-comprehensive-guide-to-python-project-management-and-packaging-concepts-illustrated-with-uv-part-i/)
- [pre-commit: install with uv](https://adamj.eu/tech/2025/05/07/pre-commit-install-uv/)
