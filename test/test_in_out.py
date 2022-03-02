from Scripts import (read_json,
                     write_json)

import os
from os.path import exists

def test_in_out():
    filein = os.path.join(os.getcwd(),'data','sample_data_input.json')
    fileout = os.path.join(os.getcwd(),'data','sample_data_output.json')
    
    req_cols = {'Gender', 'HeightCm','WeightKg'}
    
    data = read_json.main(filein, req_cols)
    print(data)
    
    write_json.main(fileout, data)
    
    assert data.shape == (5,3)
    assert set(data.columns) == req_cols
    
    assert exists(fileout)
       
    