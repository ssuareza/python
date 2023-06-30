#!/usr/bin/env sh

# autowatch and run tests
find . -name *.py | entr -n pytest &

# run app
find . -name *.py | entr -n uvicorn app.main:app --host 0.0.0.0 --port 5000
