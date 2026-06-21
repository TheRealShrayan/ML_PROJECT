import os
import sys
from src.ML_PROJECT.exception import Customexception
from src.ML_PROJECT.logger import logging
import pandas as pd
from src.ML_PROJECT.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
@dataclass
class DataIngetionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngetion:
    def __init__(self):
        self.ingetion_config=DataIngetionConfig()

    def initiate_data_ingetion(self):
        try:
            df=read_sql_data()
            logging.info("Reading completed from mysql database ")
            
            
            os.makedirs(os.path.dirname(self.ingetion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingetion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=17)
            train_set.to_csv(self.ingetion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingetion_config.test_data_path,index=False,header=True)
            logging.info("Data ingetion is completed")

            return(
                self.ingetion_config.train_data_path,
                self.ingetion_config.test_data_path
            )

        
            
            
            

        except Exception as e:
            raise Customexception(e,sys)
        

    