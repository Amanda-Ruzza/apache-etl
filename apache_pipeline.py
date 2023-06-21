import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run_pipeline():
    pipeline_options = PipelineOptions()
    with beam.Pipeline(options=pipeline_options) as pipeline:
        # Read data from a source (e.g., CSV file)
        data = (
            pipeline
            | 'ReadFromCSV' >> beam.io.ReadFromText('StrengthLog.csv')
        )
        
        # Apply transformations to process the data
        processed_data = (
            data
            | 'TransformData' >> beam.Map(lambda x: x.upper())
        )
        
        # Write the processed data to a sink (e.g., text file)
        processed_data | 'WriteToText' >> beam.io.WriteToText('apache_strength_log.csv')

if __name__ == '__main__':
    run_pipeline()
