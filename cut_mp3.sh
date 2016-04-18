in_dir='output/'
out_dir='output/'
timetable="$in_dir/times.txt"
i=1
while IFS='' read -r line; do
    echo $line| awk -v i="$i" '{split($0,a,"|"); print "cutmp3 -i " a[1] " -a " a[2] " -b " a[3] " -O result" i ".mp3"}'
    i=$((i+=1))
done < "$timetable"
