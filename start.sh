#!/bin/bash

read -p "Enter day number: " daynumber

mkdir -p "day_${daynumber}/src/part_1"
mkdir -p "day_${daynumber}/src/part_2"
mkdir -p "day_${daynumber}/src/commons"
mkdir -p "day_${daynumber}/res"
touch "day_${daynumber}/res/example.txt"
touch "day_${daynumber}/res/input.txt"
touch "day_${daynumber}/main.py"

echo "Directory structure created for day_${daynumber}."