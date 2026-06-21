from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import Customexception
import sys
from src.ML_PROJECT.components.data_ingestion import DataIngetion
from src.ML_PROJECT.components.data_ingestion import DataIngetionConfig




if __name__=="__main__":

    logging.info("The execution has started")

    try:
        #data_ingetion_config=DataIngetionConfig()
        data_ingestion=DataIngetion()
        data_ingestion.initiate_data_ingetion()

    except Exception as e:
        logging.info("Custom Exception")
        raise Customexception(e,sys)

    