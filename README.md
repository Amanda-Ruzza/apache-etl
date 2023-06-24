# Apache Beam CSV Parser
Apache Beam CSV Parser 

## How it works:
Python program that reads a CSV infile, removes empty spaces and unecessary information from a ``Log Exercise App`` and writes the **maximum weight** and **rep range** per exercise ever performed by the user into a CSV outfile.

### Running Instructions

- The original file needs to be either in the project folder
- The original file needs to have a ``Header`` 
- To run the file, execute the following command:

    ```
    python apache_pipeline.py --input <inputfilename> --output <outputfilename>   
    ```
 
 Example on how to execute this code:
    ```
    python apache_pipeline.py --input StrengthLog.csv --output max_reps.csv
    ```


#### Future Improvements