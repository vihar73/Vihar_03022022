import numpy as np
import process_json
import logging
import os

logger = logging.getLogger(__name__)

#processing json and writing output
if __name__ == "__main__":
    #input path for json file
    filein = os.path.join(os.getcwd(),'data','sample_data_input.json')

    #output path for json file
    fileout = os.path.join(os.getcwd(),'Sample','sample_data_output.json')

    #required columns in json input
    req_cols = {'Gender', 'HeightCm','WeightKg'}

    #BMI table for calculation
    bmi_list = [("Underweight",[-np.inf,18.5],"Malnutrition risk"),("Normal Weight",[18.5,25],"Low risk"),
                ("Overweight",[25,30],"Enhanced risk"),("Moderately obese",[30,35],"Medium Risk"),
                ("Severely obese",[35,40],"High risk"),("Very severely obese",[40,np.inf],"Very high risk")]

    try:
        process_json.main(filein, fileout, req_cols, bmi_list)
        
    except Exception as e:
        logger.exception('There was some issue with processing JSON. More details {0}'.format(e))

