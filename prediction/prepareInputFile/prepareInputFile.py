from prediction.models import TrainData
from prediction.api.serializer import TrainDataSerializer
import csv
import pandas as pd

class prepareDataFile:
    #get the data from the database
    def get_data():
        data = TrainData.objects.all()
        # save data in csv file
        serializer = TrainDataSerializer(data, many=True)
        serialized_data = serializer.data
        print(serializer.data)
        with open('/home/yash/Documents/cement-strength-prediction/cement_strength_prediction/prediction/prepareInputFile/input.csv', 'w') as file:
            csv_writer = csv.writer(file)
            
            # write header
            header = list(serialized_data[0].keys())
            csv_writer.writerow(header)

            # write data
            for row in serialized_data:
                csv_writer.writerow(row.values())
        df=pd.read_csv('/home/yash/Documents/cement-strength-prediction/cement_strength_prediction/prediction/prepareInputFile/input.csv')
        df.drop(df.columns[[0]], axis = 1, inplace = True)
        df.columns=['Cement _component_1','Blast Furnace Slag _component_2','Fly Ash _component_3','Water_component_4','Superplasticizer_component_5','Coarse Aggregate_component_6','Fine Aggregate_component_7','Age_day','Concrete_compressive _strength']
        df.to_csv('/home/yash/Documents/cement-strength-prediction/cement_strength_prediction/prediction/prepareInputFile/input.csv',index=False)
