# OpenAPI Generated Clients for _CUBE_

This repository contains client libraries for the [_ChRIS_ backend](https://github.com/fnndsc/ChRIS_ultron_backEnd)
created using the [OpenAPI generator](https://openapi-generator.tech/).

## Documentation

| Package        | Language | Description                                     |
|----------------|----------|-------------------------------------------------|
| [aiochris-oag] | Python   | Python client based on [asyncio] and [aiohttp]. |
| [chris-oag]    | Python   | Python client based on [urllib3].               |

[aiochris-oag]: ./python-async/README.md
[chris-oag]: ./python/README.md
[asyncio]: https://docs.python.org/3/library/asyncio.html
[aiohttp]: https://docs.aiohttp.org
[urllib3]: https://urllib3.readthedocs.io

## Releasing

It would be nice for this to be fully automated, but currently it is not. https://github.com/FNNDSC/ChRIS_ultron_backEnd/issues/587

When a breaking release is made in https://github.com/FNNDSC/ChRIS_ultron_backEnd...

```shell
git clone git@github.com:FNNDSC/openapi-clients.git
cd openapi-clients

echo "1.2.3" > version.txt  # increase the value of version.txt as appropriate
just  # regenerate all client code

git add -A
git commit -m "Version $(< version.txt)"
git push origin main
```

## Adding A Generator

Many other generators are available. See the list here: https://openapi-generator.tech/docs/generators

To add a generator, create a YAML configuration file for it in `configs`.

## Hacks

The [rust generator](https://openapi-generator.tech/docs/generators/rust/) is lacking for several reasons:

- Produces `Option<Option<_>>`, which is partially fixed by upgrading to `openapi: 3.1.0` https://github.com/OpenAPITools/openapi-generator/issues/16283
- Does not support `additionalProperties` https://github.com/OpenAPITools/openapi-generator/issues/20965 https://github.com/OpenAPITools/openapi-generator/issues/19989
- Bug calling `format!()` with `Option<T>` https://github.com/OpenAPITools/openapi-generator/issues/20145
- Produces non-compiling code https://github.com/OpenAPITools/openapi-generator/issues/19923
- Subjectively, the code produced contains a lot of nonsense

To avoid these problems, we:

1. Avoid generating the Rust client, produce [serde](https://serde.rs/) models only
2. Apply manual patches to fix models
