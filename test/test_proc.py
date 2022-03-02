from Scripts import (read_json,
                     helpers)
import numpy as np
import os

def test_proc():
    filein = os.path.join(os.getcwd(),'data','sample_data_input.json')
    
    req_cols = {'Gender', 'HeightCm','WeightKg'}
    bmi_list = [("Underweight",[-np.inf,18.5],"Malnutrition risk"),("Normal Weight",[18.5,25],"Low risk"),
                ("Overweight",[25,30],"Enhanced risk"),("Moderately obese",[30,35],"Medium Risk"),
                ("Severely obese",[35,40],"High risk"),("Very severely obese",[40,np.inf],"Very high risk")]
    
    data = read_json.main(filein, req_cols)
    print(data)
    data['Gender'] = data['Gender'].apply(helpers.parse_string)
    data['HeightCm'] = data['HeightCm'].apply(helpers.parse_float)
    data['WeightKg'] = data['WeightKg'].apply(helpers.parse_float)
    (data['BMI'], data['BMI_Category'], data['Health Risk']) = zip(*data.apply(lambda x: helpers.bmi_calc(bmi_list,x['HeightCm'],x['WeightKg']),
                                                                                               axis=1))
    assert data['HeightCm'].dtype == np.float64
    assert data['WeightKg'].dtype == np.float64
    assert data['BMI'][0] == 32.8
    assert data['BMI_Category'][2] == 'Normal Weight'
    assert data['Health Risk'][3] == 'Low risk'
    
