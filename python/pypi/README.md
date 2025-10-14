# Python PyPI

## Python PyPI tools

- [Oven](https://pyoven.org/)
- [PyPi Browser](https://pypi-browser.org/)

## Related links

- [Publishing to PyPI with a Trusted Publisher](https://docs.pypi.org/trusted-publishers/)
- [Attestations: A new generation of signatures on PyPI](https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/)

## PyPI API

```shell
curl -s "https://pypi.org/simple/<package-name>/?format=application/vnd.pypi.simple.v1+json" | jq
```
