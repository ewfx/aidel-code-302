from model.process_input_data import process_file
from model.entity_prediction import predict_entity
input_file = "./src/data/input_data/unstructured_data.json"  # Change this to the appropriate file
output_file = "./src/data/output_data/processed_output.csv"
file_path = "./src/data/output_data/processed_output.csv"

process_file(input_file, output_file)
predict_entity(file_path)