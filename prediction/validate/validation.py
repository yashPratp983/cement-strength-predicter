import os
import pandas as pd
import json
from prediction.models import TrainData
from prediction.api.serializer import TrainDataSerializer

class validation:
    def __init__(self, request):
        self.request = request
    
    # Function to validate a row against the expected format
    def validate_row(row,expected_format):
        # Check the number of columns
        if len(row) != expected_format["NumberofColumns"]:
            return False

        # Check each column against the expected type
        for col_name, col_type in expected_format["ColName"].items():
           
            if col_name not in row:
                print("Column name not found in row")
                return False

            if col_type == "FLOAT" and not pd.api.types.is_float_dtype(row[col_name]):
                print("Column is not float")
                return False
            elif col_type == "INTEGER" and not pd.api.types.is_integer_dtype(row[col_name]):
                # return true if row[col_name] if it is of float type and ends with .0
                if pd.api.types.is_float_dtype(row[col_name]) and str(row[col_name]).endswith(".0"):
                    return True
                return False

        return True

    def call():
        # This is where the actual logic of the template tag would happen
        # read all the files in the directory
        expected_format = {}
        with open('/home/yash/Documents/cement-strength-prediction/cement_strength_prediction/schema_training.json', 'r') as file:
            expected_format = json.load(file)
        print(expected_format)
        path="/home/yash/Documents/cement-strength-prediction/cement_strength_prediction/cement_strength_prediction/Training_Batch_Files"
        list_of_files = os.listdir(path)
        good_data = []
        bad_data = []
        for file in list_of_files:
            # Read the file
            df = pd.read_csv(path+"/"+file)
            # Validate each row
            for index, row in df.iterrows():
                print(row)
                print(file)
                if validation.validate_row(row,expected_format):
                    # print("reached")
                    good_data.append(row)
                else:
                    bad_data.append(row)
        
        # save the good data to the database
        for row in good_data:
            serializer = TrainDataSerializer(data={
                "cement": row["Cement _component_1"],
                "blast_furnace_slag": row["Blast Furnace Slag _component_2"],
                "fly_ash": row["Fly Ash _component_3"],
                "water": row["Water_component_4"],
                "superplasticizer": row["Superplasticizer_component_5"],
                "coarse_aggregate": row["Coarse Aggregate_component_6"],
                "fine_aggregate": row["Fine Aggregate_component_7"],
                "age": row["Age_day"],
                "strength": row["Concrete_compressive _strength"],
            })
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
        print(len(good_data))
        print(len(bad_data))
        return "Hello World"