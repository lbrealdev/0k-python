# uv: An extremely fast Python package and project manager, written in Rust.

### Setup

Installing `uv`:
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

To enable shell autocompletion for uv commands, run one of the following:
```shell
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
```

Unistalling `uv`:
```shell
rm ~/.cargo/bin/uv ~/.cargo/bin/uvx
```

Install a specific Python version:
```shell
uv python install 3.12
```

Update uv to the latest version:
```shell
uv self update
```

### Source

- Website: https://docs.astral.sh/uv/
- GitHub Repository: https://github.com/astral-sh/uv

### Blogs

- [uv: Unified Python packaging from Astral](https://astral.sh/blog/uv-unified-python-packaging)
- [uv: Unified Python packaging from Simon Willison](https://simonwillison.net/2024/Aug/20/uv-unified-python-packaging/)
- [Python: my new uv setup for development](https://adamj.eu/tech/2024/09/18/python-uv-development-setup/)
- [Switching from pyenv to uv](https://bluesock.org/~willkg/blog/dev/switch_pyenv_to_uv.html)
- [Docker images using uv's python](https://mkennedy.codes/posts/python-docker-images-using-uv-s-new-python-features/)
- [Production-ready Docker Containers with uv](https://hynek.me/articles/docker-uv/)
- [Switching from virtualenvwrapper to direnv, Starship, and uv](https://treyhunner.com/2024/10/switching-from-virtualenvwrapper-to-direnv-starship-and-uv/)
- [A comprehensive guide to python project management and packaging concepts illustrated with uv part 1](https://reinforcedknowledge.com/a-comprehensive-guide-to-python-project-management-and-packaging-concepts-illustrated-with-uv-part-i/)
