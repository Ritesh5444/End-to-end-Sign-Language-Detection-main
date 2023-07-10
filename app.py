from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.logger import logging

logging.info("Entered the app.py")

obj = TrainPipeline()
logging.info("Entered the app.py > obj creation done")

obj.run_pipeline()

print("Training pipeline finished!")
