## Operator Authorization Qualifier

This directory contains an automated test for qualifying Operator Data checks for Flight Authorization compliance. 

### What is tested? 

As of `November 2021` the test primarily covers checking of a valid `UAS serial number` and a valid `Operator registration number`. A payload is generated that can contain valid or invalid (per the relevant standards) data, the USSP has to respond to the test saying if the payload passed validation (or not). At this moment, we do not cover why the validation failed, just a message that the processing has passed or failed. 

### Files 
- `operator_data_generator.py` : This is the main data generation module for the test. This module generates valid sample data for the test. 
- `test_executor.py`: This module utilizes the data generator to generate 
- `Reference Implementation` : If you want to see a reference implementation to compare your results against, you can see it in the [Aerobridge](https://github.com/openskies-sh/aerobridge) operations management server.  

### Running the test

The test can be run using the `run_locally.sh` command. The command will look for a config.json file that needs to be created to point the test infrastructure to the USSP endpoint. The test uses OAUTH tokens / authorization scheme and comes with a dummy OAUTH server to issue tokens.