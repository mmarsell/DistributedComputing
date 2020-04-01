OUTPUT_DIR=/user/${USER}/assignment/task3
OUTPUT_TEMP_DIR=/user/${USER}/assignment/task3temp
OUTPUT_TEMP_FILE=outputTemp.out
OUTPUT_FILE=output.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_TEMP_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator='|' \
    -D stream.map.output.field.separator='|' \
    -D stream.num.map.output.key.fields=4 \
    -D num.key.fields.for.partition=1 \
    -D mapreduce.partition.keypartitioner.options='-k1,1' \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input /data/large/imdb/title.basics.tsv \
    -input /data/large/imdb/title.ratings.tsv \
    -output $OUTPUT_TEMP_DIR \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py

hdfs dfs -rm -r $OUTPUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.map.output.key.field.separator='|' \
    -D stream.map.output.field.separator='|' \
    -D stream.num.map.output.key.fields=4 \
    -D num.key.fields.for.partition=1 \
    -D mapreduce.partition.keypartitioner.options='-k1,1' \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input ${OUTPUT_TEMP_DIR}/ \
    -output $OUTPUT_DIR \
    -mapper mapper2.py \
    -reducer reducer2.py \
    -file mapper2.py \
    -file reducer2.py

hdfs dfs -rm -r $OUTPUT_TEMP_DIR
hdfs dfs -cat ${OUTPUT_DIR}/part-00000 | head -20 > $OUTPUT_FILE
