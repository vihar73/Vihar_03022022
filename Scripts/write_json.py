import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main(filename, df):
    '''
    Parameters
    ----------
    filename : Output source (in this case file on local);
    df : Dataframe to write

    Returns
    -------
    None.
    
    '''
    try:
        logger.info("Writing data to JSON")
        df.to_json(filename, orient='records', lines=True)
    except Exception as e:
        logger.exception("Error while writing json output. More details {0}".format(e))