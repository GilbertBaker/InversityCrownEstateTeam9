#!/bin/bash
source .venv/bin/activate
flask --app server run --debug&
PIDS[0]=$!
scss --watch deploy/style.scss&
PIDS[1]=$!

trap "kill ${PIDS[*]}" SIGINT

wait
