from textSummerizer.logging import logger
from textSummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n xxxx============xxxx")

except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n xxxx============xxxx")

except Exception as e:
    logger.exception(e)
    raise e    