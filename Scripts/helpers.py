import logging

logger = logging.getLogger(__name__)

def parse_float(f):
    '''
    Returns float or zero
    
    '''
    try:
        f = float(f)
    except Exception:
        f == 0
    return f

def parse_string(s):
    '''
    Returns string or empty
    
    '''
    try:
        s = str(s)
    except Exception:
        s == ''
    return s

def bmi_calc(bmi_list, height, weight):
    '''
    Parameters
    ----------
    bmi_list : mapping table for BMI categories;
    height : Height in cm;
    weight : Weight in Kg

    Returns
    -------
    bmi : BMI of person;
    tag : BMI tag as per mapping table;
    risk : Heatlh risk as per mapping table

    '''
    try:
        bmi = weight/(height/100)**2    
        bmi = round(bmi,1)
        
        for tag, rng, risk in bmi_list:
            if bmi >= rng[0] and bmi < rng[1]:
                return bmi, tag, risk
    except Exception as e:
        logger.exception("Error while processing BMI calculations. Please check BMI mapping list. More details {0}".format(e))