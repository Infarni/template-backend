#!/bin/sh

current_script_path="$(realpath "$0")"

directory_path="$(dirname "$current_script_path")"

project_dir_path="$(dirname "$directory_path")"

cd "$project_dir_path" || exit

DEBUG=${DEBUG:-false}
PORT=${PORT:-8000}

if [ "$DEBUG" = true ]; then
    echo "DEBUG is true. Executing in debug mode"
    poetry run fastapi dev --host 0.0.0.0 --port $PORT --reload rps_backend/main.py
else
    echo "DEBUG is false. Executing prod mode"
    poetry run fastapi run --host 0.0.0.0 --port $PORT --workers 4 rps_backend/main.py
fi
