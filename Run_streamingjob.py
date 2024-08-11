# run for data preparation
hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-input /user/hadoop/dataset/Books_rating.csv \
-output /user/hadoop/output/preprocessed_books_rating \
-mapper /home/hadoop/assignment/preprocess/preprocess_mapper.py \
-file /home/hadoop/assignment/preprocess/preprocess_mapper.py \
-file /home/hadoop/assignment/preprocess/stopwords.txt \
-numReduceTasks 0

# run for wordcount
hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-input /user/hadoop/output/preprocessed_books_rating \
-output /user/hadoop/output/wordcount_output \
-mapper wordcount_mapper.py \
-reducer wordcount_reducer.py \
-file wordcount_mapper.py \
-file wordcount_reducer.py

# run for sentiment analysis
hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files vader_lexicon.txt,sentiment_analysis_mapper.py,sentiment_analysis_reducer.py \
-mapper "python3 sentiment_analysis_mapper.py" \
-reducer "python3 sentiment_analysis_reducer.py" \
-input /user/hadoop/output/preprocessed_books_rating \
-output /user/hadoop/output/sentiment_output

