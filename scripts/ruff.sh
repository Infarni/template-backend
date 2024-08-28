#!/bin/sh

current_script_path="$(realpath "$0")"

directory_path="$(dirname "$current_script_path")"

project_dir_path="$(dirname "$directory_path")"

cd "$project_dir_path" || exit

set -x

poetry run ruff format --config "$project_dir_path/pyproject.toml"
