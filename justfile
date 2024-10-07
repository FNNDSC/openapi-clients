file := "schema_split.yaml"
releases_url := "https://github.com/FNNDSC/ChRIS_ultron_backEnd/releases"

generate-all:
    @just generate python           -g python       -p packageName=chris_oag,projectName=chris-oag         -p library=urllib3,packageVersion=$(just get-version-pep440)
    @just generate python-async     -g python       -p packageName=aiochris_oag,projectName=aiochris-oag   -p library=asyncio,packageVersion=$(just get-version-pep440)
    # @just generate typescript-fetch -g typescript-fetch -p npmName=@fnndsc/chris-openapi-generated -p withInterfaces=true
    # @just generate rust             -g rust         -p packageName=chris-openapi-generated                           -p library=reqwest,preferUnsignedInt=true,supportMiddleware=true

# generate an OpenAPI client
generate output +options:
    @if ! [ -e "{{file}}" ]; then \
      error="$(tput setaf 1)error$(tput sgr0): {{file}} not found."; \
      suggestion="Please download the OpenAPI specification YAML from {{releases_url}} and save it as $(pwd)/{{file}}"; \
      echo "$error $suggestion"; \
      exit 1; \
    fi
    if ! [ -d {{output}} ]; then mkdir -v {{output}}; fi
    podman run --rm --userns=keep-id:uid=100100,gid=100100 -u 100100:100100 \
        -v "$(pwd)/{{output}}:/out:rw" -v "$(pwd)/{{file}}:/{{file}}:ro" \
        docker.io/openapitools/openapi-generator-cli:v7.8.0 \
        generate {{options}} -i "/{{file}}" -o "/out"

get-version-pep440:
    @./semver2pep440.sh < version.txt

get-version:
    @cat version.txt

