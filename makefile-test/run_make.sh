#!/bin/bash

echo ""
make setup

echo ""
make lint

echo ""
make format

echo ""
make run-script

echo ""
make run-script2
