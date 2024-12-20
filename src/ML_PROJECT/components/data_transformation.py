import sys
from dataclasses import dataclass
import numpy as np 
import pandas as pd 

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.utils import save_object
import os

@dataclass

class DataTransformationConfig:
    preprocessor_obj_file_path= os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        this function is responsible for data transformation 
        '''
        try:
            cat_features=['gender',
                          'race/ethnicity',
                          'parental level of education',
                          'lunch',
                          'test preparation course']
            num_features=['reading score', 'writing score']

            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

            ])
            cat_pipeline=Pipeline(steps=[
                ("imputer" ,SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scalar",StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical Colums:{cat_features}")
            logging.info(f'Numerical Columns: {num_features}')

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,num_features),
                    ('cat_pipeline',cat_pipeline,cat_features)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)
            logging.info("Reading the train and test file")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math score"
            num_features=['reading score', 'writing score']
            # divide dataset into independent and dependent feature
            input_features_train_df=train_df.drop(columns=[target_column_name],axis=1)

            target_feature_train_df=train_df[target_column_name]
            
            ## divide dataset into independent and dependent feature
            input_features_test_df=train_df.drop(columns=[target_column_name],axis=1)

            target_feature_test_df=train_df[target_column_name]

            logging.info("Applying preprocessintg on training and test set")

            input_features_train_arr=preprocessing_obj.fit_transform(input_features_train_df)
            input_features_test_arr=preprocessing_obj.transform(input_features_test_df)
            # we only use transform in test because of data leakage prevention

            train_arr=np.c_[input_features_train_arr,np.array(target_feature_train_df)]

            test_arr=np.c_[input_features_test_arr,np.array(target_feature_test_df)]
             
            logging.info("Saved preprocessing object")

            save_object(self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessing_obj)
            
            return (
                train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)