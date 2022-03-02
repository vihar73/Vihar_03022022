import pandas as pd
import ijson
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main(filename, req_cols, low_memory = False):
    '''
    Parameters
    -----------------------------
    filename : input buffer (in this case local file);
    req_cols : required set of columns in the final dataframe;
    low_memory : True/False - read the input line by line or load all in memory at once
    
    Returns
    -----------------------------
    read_data : Dataframe with json data (chose dataframe as preferred option so if required - can easily add more complex transformations and manipulations if required as per update in any requirements)
    
    '''
    if not low_memory:
        try:
            logger.info("Reading all json data")
            with open(filename,'r') as f:
                read_data = pd.read_json(f, orient="records")
            unreq_cols = set(read_data.columns) - set(read_data.columns).intersection(req_cols)
            if len(unreq_cols) > 0:
                logger.info("Dropping unrequired columns")
                read_data.drop(list(unreq_cols), axis = 'columns', inplace=True)
        except:
            read_data = pd.DataFrame(columns=list(req_cols))
    else:
        try:
            read_data = pd.DataFrame(columns=list(req_cols))
            logger.info("Low memory option: reading json line by line. This will take more time, but is more memory efficient")
            with open(filename, "r") as f:
                for col in req_cols:
                    data = ijson.items(f, 'item.{}'.format(col))
                    data_list = [i for i in data]
                    read_data[col] = data_list
        except Exception as e:
            logger.exception("Error in reading JSON data into dataframe. Returning empty dataframe by default. More details: {0}".format(e))
            read_data = pd.DataFrame(columns=list(req_cols))       
    
    return read_data