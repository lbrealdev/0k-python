# Rye: a Hassle-Free Python Experience

Rye is a comprehensive project and package management solution for Python.

## Sources

- Website: https://rye.astral.sh/
- GitHub Repository: https://github.com/astral-sh/rye

### Usage

Installing `rye`:
```shell
curl -fsSL https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash
```

Add `shims` to path:
```shell
echo 'source "$HOME/.rye/env"' >> ~/.bashrc
```

Update `rye`:
```shell
rye self update
```

Uninstalling `rye`:
```shell
rye self uninstall
```

## Related links

- [Rye and uv: August is Harvest Season for Python Packaging](https://lucumr.pocoo.org/2024/8/21/harvest-season/)
