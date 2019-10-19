#!/bin/bash

sed -i '.orig' -e "s/MyClass/${1}/g" a.cpp
sed -i '.orig' -e "s/MyFunc/${2}/g" a.cpp
rm a.cpp.orig
