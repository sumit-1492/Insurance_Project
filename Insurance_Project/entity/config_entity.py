import os, sys
from Insurance_Project.exception import InsuraneceException
from Insurance_Project.logger import logging
from datetime import datetime

FILE_NAME = "insurance.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME =  "test.csv"
#TRANSFORMER_OBJECT_FILENAME = "transformer.pkl"

class TrainingPipelineconfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise InsuraneceException(e,sys)

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineconfig):
        try:
            self.database_name = "Insurance1"
            self.collection_name = "Insurance_Project1"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise InsuraneceException(e,sys)

#convertin data to dictionary for reading in terminal
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise InsuraneceException(e,sys)

#class DataValidationConfig:
    #def __init__(self,training_pipeline_config:TrainingPipelineconfig):
        #self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
        #self.report_file_path = os.path.join(self.data_validation_dir,"report.yaml") ## reeport file can be csv, or yaml or json
        #self.missing_threshold:float = 0.2
        #self.base_file_path = os.path.join("insurance.csv")