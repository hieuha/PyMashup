in_dir='output'
out_dir='output'
timetable="$in_dir/times.txt"
i=1
while IFS='' read -r line; do
    result="$out_dir/result$i.mp3"
    split_command=`echo $line| awk -v result="$result" '{split($0,a,"|"); print "cutmp3 -i " a[1] " -a " a[2] " -b " a[3] " -O " result'}`
    $split_command
    i=$((i+=1))
done < "$timetable"
results=`ls $out_dir/result*.mp3`
results_concat=`echo "concat:"$results|sed 's/ /|/g'`
echo $results_concat
ffmpeg -i "$results_concat" -acodec copy "$out_dir/output.mp3"
