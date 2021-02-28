#!/bin/bash
for file in ./datos/*
do
    if [[ -f $file ]]; then
       echo $file
       fn_date=$(echo $file | cut -f 3 -d '/' | cut -c 28-35)
       echo $fn_date
       split_date=$(echo ${fn_date:0:4}-${fn_date:4:2}-${fn_date:6:2}T00:00:42)
       echo $split_date
       cp $file estructura_autoridades_apn.csv
       git add estructura_autoridades_apn.csv
       GIT_AUTHOR_DATE=$split_date GIT_COMMITTER_DATE=$split_date git commit -m "Cambios $fn_date"
    fi
done
