#!/bin/bash

pytest --cov src &> tmp

cat << EOF > __.py
#!/usr/bin/python3 -tt
with open('tmp') as tmp:
    for line in tmp:
        line = line.strip()
        if "TOTAL" in line:
            cov = int(line.replace('%', '').split()[-1])
            if cov >= int(VALUE):
                print("pass")
            else:
                print("\nFailed to achieve %VALUE coverage")

EOF

sed -i "s/VALUE/$1/g" __.py
chmod 770 __.py
./__.py
rm __.py
rm tmp
