import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.pipeline.training_pipeline import TrainingPipeline


# method for start training
def start_training():
    try:
        # create object of Trainingpipline class and
        # for running entire pipeline exceute run pipeline function  
        model_training = TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    start_training()