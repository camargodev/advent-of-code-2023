#!/bin/bash

read -p "$(tput bold)Enter day number: $(tput sgr0)" daynumber
read -p "$(tput bold)Enter file name (without extension): $(tput sgr0)" filename
read -p "$(tput bold)Enter method name: $(tput sgr0)" methodname

# Generate class name from filename (capitalize each word, remove underscores, and remove spaces)
classname=$(echo "${filename}" | tr '_' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2));}1' | tr -d ' ')

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

echo -e "\n$(tput bold)$(tput setaf 2)Folder ${base_path} with files ${filename}.py and main.py created successfully.$(tput sgr0)"
echo "To execute main.py, run the following command:"
echo "$(tput setaf 3)python3 ${base_path}/main.py$(tput sgr0)"