from pyspark import SparkContext

sc = SparkContext()

text_file = sc.textFile("gs://dataproc-sample-byjw/input.txt")

counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

for data in counts.collect():
    print(data)
