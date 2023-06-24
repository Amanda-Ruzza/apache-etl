import logging
import argparse
import re # find the regular expressions for the unnecessary words to remove
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run_pipeline(argv=None):

  """Main entry point; defines and runs the CSV parser pipeline."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--input',
    dest='input',
    help='Input file to process.')
  parser.add_argument(
    '--output',
    dest='output',
    required=True,
    help='Output file to write results to.')
  known_args, pipeline_args = parser.parse_known_args(argv)

  pipeline_options = PipelineOptions(pipeline_args)
  
  regex_value = r'Exercise, '
  # The pipeline will be run on exiting the 'with' block.    
  with beam.Pipeline(options=pipeline_options) as pipeline:
    # Read data from a source (e.g., CSV file)
    data = (
            pipeline
            | 'ReadFromCSV' >> beam.io.ReadFromText(known_args.input)
        )
        
    # Apply transformations to process the data
    processed_data = (
            data 
            # |'TransformData' >> beam.Map(lambda x: x.upper())
            |'Strip' >> beam.Map(lambda x: x.strip(','))
            |'Strip header' >> beam.Map(lambda text: text.strip('# \n'))
            # |'StripExerciseName' >> beam.Map(lambda ex: ex.strip('Exercise, '))
            |'CleanExerciseName' >> beam.Regex.replace_all(regex_value, '')
        )
        
        # Write the processed data to a sink (e.g., text file)
    processed_data | 'WriteToText' >> beam.io.WriteToText(known_args.output)
    processed_data | 'PrintToConsole' >> beam.Map(print)




if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run_pipeline()
