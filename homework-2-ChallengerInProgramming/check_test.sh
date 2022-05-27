#!/bin/bash

input=$1
d="_$((1 + $RANDOM % 100))"
mkdir -p $d
echo "import importlib" > $d/test_all.py
echo "_ = importlib.import_module('_')" >> $d/test_all.py
cat test/test_all.py >> $d/test_all.py
touch $d/__init__.py
sed -i "s/src/_/g" $d/test_all.py
passed_on_correct=$(pytest -k $input | grep $input | grep "PASSED" | wc -l)
failed_on_incorrect=$(pytest $d -k $input | grep $input | grep "^FAILED" | wc -l)

if [ $passed_on_correct -eq "0" ];
then
    echo -e "\n\ntest:$input failed to test the source code.";
    rm -rf $d;
    exit 0;
else
    if [ $failed_on_incorrect -eq "1" ];
    then
        echo "pass";
        rm -rf $d;
        exit 0;
    else
        echo -e "\n\ntest:$input unexpectedly passed on incorrect source code, it should have failed!";
        rm -rf $d;
        exit 0;
    fi
fi
