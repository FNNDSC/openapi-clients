# OpenAPI Generated Clients for _CUBE_

This repository contains client libraries for the [_ChRIS_ backend](https://github.com/fnndsc/ChRIS_ultron_backEnd)
created using the [OpenAPI generator](https://openapi-generator.tech/).

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
