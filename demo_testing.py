import sys

from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.exception import HousingExcecption
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)

        # schema_file_path = r"E:\MStudy material\iTech\iNeuron\Projects\ML projects\Machine_Learning_Project_01\config\schema.yaml"
        # file_path =  r"E:\MStudy material\iTech\iNeuron\Projects\ML projects\Machine_Learning_Project_01\housing\artifact\data_ingestion\2022-08-28-11-35-55\ingested_data\train\housing.csv"

        # df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

     



if __name__ == "__main__":
    main()