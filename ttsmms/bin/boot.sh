#!/usr/bin/env sh

# autowatch and run tests
find . -name *.py | entr -r pytest &

# run app
find . -name *.py | entr -r uvicorn app.main:app --host 0.0.0.0 --port 5000
