#!/usr/bin/env bash
# Commands to call for task checks

echo "./0-fizzbuzz.py 50"
./0-fizzbuzz.py 50
echo "./1-print_square.js 4"
./1-print_square.js 4
echo "./1-print_square.js 10"
./1-print_square.js 10
echo "ruby 2-sort.rb 12 41 2 C 9 -9 31 fun -1 32"
ruby 2-sort.rb 12 41 2 C 9 -9 31 fun -1 32
echo "./3-user.py"
./3-user.py
echo "cd 4-delete_dnodeint"
cd 4-delete_dnodeint/
echo "gcc -Wall -pedantic -Werror -Wextra -std=gnu89 main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c -o delete_dnodeint"
gcc -Wall -pedantic -Werror -Wextra -std=gnu89 main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c delete_dnodeint_at_index.c -o delete_dnodeint

echo "./delete_dnodeint"
./delete_dnodeint

cd ..
