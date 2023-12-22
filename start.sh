#!/bin/bash

read -p "Enter day number: " daynumber
read -p "Enter file name (without .py): " filename

base_path="day_${daynumber}"

mkdir -p "${base_path}/src/part_1"
mkdir -p "${base_path}/src/part_2"
mkdir -p "${base_path}/src/commons"
mkdir -p "${base_path}/res"

touch "${base_path}/res/example.txt"
touch "${base_path}/res/input.txt"
touch "${base_path}/main.py"

touch "${base_path}/src/part_1/${filename}.py"
touch "${base_path}/src/part_2/${filename}.py"

echo "Directory structure created for ${base_path} and file ${filename} created in part_1 and part_2."
