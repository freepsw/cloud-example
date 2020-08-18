from __future__ import print_function
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

pipeline_options = PipelineOptions(
    project='snappy-helper-239504', # Project ID
    runner='dataflow',              # GCP Dataflow에서 돌리기 위함
    temp_location='gs://dataflow-sample-byjw/temp'
)

with beam.Pipeline(options=pipeline_options) as p:
  p | 'Read' >> beam.io.ReadFromText("gs://dataflow-sample-byjw/uptownfunk.txt") \
    | 'Extract' >> beam.FlatMap(lambda s: re.split("\\W+", s)) \
    | 'Count' >> beam.combiners.Count.PerElement() \
    | 'Map' >> beam.Map(lambda (w, c): "%s: %d" % (w, c)) \
    | 'Save' >> beam.io.textio.WriteToText("gs://dataflow-sample-byjw/output.txt")
