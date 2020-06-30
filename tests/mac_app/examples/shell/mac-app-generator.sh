#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set -- "${BASH_SOURCE[0]%/*}"/.script.sh /tmp/shell.app
( set -x; mac-app-generator "$@" )

set -- "${BASH_SOURCE[0]%/*}"/.script.sh /tmp/shell-image.app "${BASH_SOURCE[0]%/*}"/image.png
( set -x; mac-app-generator "$@" )
