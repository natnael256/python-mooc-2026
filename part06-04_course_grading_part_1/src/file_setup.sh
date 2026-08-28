for item in \ 
    "exercises1" \
    "exercises2" \
    "students1" \
    "students2"
    do
        set -- $item
        touch "${1}.csv"
done