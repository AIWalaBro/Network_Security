import os
import sys


"""
Data Ingestion related constant start with Data_INGESTION VAR NAME
"""
TARGET_COLUMN     = "Result"
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR:str  = "Artifacts"
FILE_NAME:str     = "NetworkData.csv"


TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str  = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME  = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")
SCHEMA_DROP_COLS = "drop.columns"

SAVED_MODEL_DIR = os.path.join("saved_models")

"""
Data Validation related constant start with Data_Validation VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "Network_Security_Collection"
DATA_INGESTION_DATABASE_NAME:str = "AIWalaBro_Database"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""
Data Transformation related constant start with Data_Transformation VAR NAME
"""

"""
Model Trainer related constant start with Model Trainer VAR NAME
"""