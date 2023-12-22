#!/bin/bash

read -p "Enter day number: " daynumber
read -p "Enter file name: " filename
read -p "Enter class name: " classname
read -p "Enter method name: " methodname

base_path="day_${daynumber}"
python_code=$(cat <<EOF
class ${classname}:
    def ${methodname}(self, lines):
        pass
EOF
)

mkdir -p "${base_path}/src/part_1"
mkdir -p "${base_path}/src/part_2"
mkdir -p "${base_path}/src/commons"
mkdir -p "${base_path}/res"

touch "${base_path}/res/example.txt"
touch "${base_path}/res/input.txt"
touch "${base_path}/main.py"

echo "${python_code}" > "${base_path}/src/part_1/${filename}.py"
echo "${python_code}" > "${base_path}/src/part_2/${filename}.py"

echo "Directory structure created for ${base_path} and file ${filename} created with custom Python code."
