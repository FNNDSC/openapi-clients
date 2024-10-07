#!/usr/bin/env sh

set -e

assert () {
  if [ "$1" != "$2" ]; then
    echo "$1 != $2"
    exit 1
  fi
}

assert "$(echo 1.2.3         | ./semver2pep440.sh)" '1.2.3'
assert "$(echo 1.2.3-alpha.4 | ./semver2pep440.sh)" '1.2.3a4'
assert "$(echo 1.2.3-beta.5  | ./semver2pep440.sh)" '1.2.3b5'
