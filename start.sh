#!/bin/bash

read -p "Enter day number: " daynumber
read -p "Enter file name (without extension): " filename
read -p "Enter class name: " classname
read -p "Enter method name: " methodname

base_path="day_${daynumber}"
parts_code=$(cat <<EOF
class ${classname}:
    def ${methodname}(self, lines):
        pass
EOF
)

main_code=$(cat <<EOF
from src.part_1.${filename} import ${classname} as First${classname}
from src.part_2.${filename} import ${classname} as Second${classname}

if __name__ == "__main__":
    lines = [line.replace("\n","") for line in open("day_${daynumber}/res/example.txt", "r")]
    print(First${classname}().${methodname}(lines))
    print(Second${classname}().${methodname}(lines))
EOF
)

mkdir -p "${base_path}/src/part_1"
mkdir -p "${base_path}/src/part_2"
mkdir -p "${base_path}/src/commons"
mkdir -p "${base_path}/res"

touch "${base_path}/res/example.txt"
touch "${base_path}/res/input.txt"
touch "${base_path}/main.py"

echo "${parts_code}" > "${base_path}/src/part_1/${filename}.py"
echo "${parts_code}" > "${base_path}/src/part_2/${filename}.py"
echo "${main_code}" > "${base_path}/main.py"

echo "Directory structure created for ${base_path}, file ${filename}.py created, and main.py filled with custom Python code."
echo "To execute main.py, run the following command:"
echo "python3 ${base_path}/main.py"
