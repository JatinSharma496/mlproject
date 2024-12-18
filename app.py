from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import CustomException
import sys
from src.ML_PROJECT.components.data_ingestion import DataIngestion

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)