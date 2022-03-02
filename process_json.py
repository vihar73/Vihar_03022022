import pandas as pd
import ijson
import logging
from Scripts import (read_json,
                     write_json,
                     helpers)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
       
def main(filein, fileout, req_cols, bmi_list):
    '''
    Parameters
    ----------
    filein : Path/address to input file/buffer;
    fileout : Path/address to output file/buffer;
    req_cols : columns to process in json;
    bmi_list : BMI chart map

    Returns
    -------
    Writes a json file (line wise) to fileout path/buffer
    
    '''
    
    bmi_data = read_json.main(filein, req_cols)
    
    bmi_data['Gender'] = bmi_data['Gender'].apply(helpers.parse_string)
    bmi_data['HeightCm'] = bmi_data['HeightCm'].apply(helpers.parse_float)
    bmi_data['WeightKg'] = bmi_data['WeightKg'].apply(helpers.parse_float)
    (bmi_data['BMI'], bmi_data['BMI_Category'], bmi_data['Health Risk']) = zip(*bmi_data.apply(lambda x: helpers.bmi_calc(bmi_list,x['HeightCm'],x['WeightKg']),
                                                                                               axis=1))
    print("Number of people in each BMI category: ")
    print(bmi_data['BMI_Category'].value_counts())
    
    write_json(fileout, bmi_data)