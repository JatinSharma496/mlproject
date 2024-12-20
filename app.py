from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import CustomException
import sys
from src.ML_PROJECT.components.data_ingestion import DataIngestion
from src.ML_PROJECT.components.data_transformation import DataTransformation
if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)