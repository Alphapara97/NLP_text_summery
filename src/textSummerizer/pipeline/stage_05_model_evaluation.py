
from textSummerizer.logging import logger
from textSummerizer.config.configuration import ConfigrationManager
from textSummerizer.components.model_evaluation import ModelEvaluation




class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigrationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()