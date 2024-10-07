#!/usr/bin/env sh
# Converts alpha/beta version suffix from semantic versioning 2.0.0 to PEP 440

sed 's/-beta\./b/' | sed 's/-alpha\./a/'
