#!/bin/bash

function git_sparse_clone() (
  rurl="$1" branch="$2" localdir="$3" && shift 3

  mkdir -p "$localdir"
  cd "$localdir" || exit

  git init
  git remote add -f origin "$rurl"

  git config core.sparseCheckout true

  # Loops over remaining args
  for i; do
    echo "$i" >>.git/info/sparse-checkout
  done

  git pull origin "$branch"
)

if [ "$1" == "git-sparse-checkout" ]; then
  shift 1
  git_sparse_clone "$@"
else
  "$@" || exit
fi
