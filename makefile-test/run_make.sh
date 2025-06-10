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

# 파일을 지정해서 실행하기
echo ""
make -f Makefile.test mytask
