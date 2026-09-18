import argparse
import logging

from src.genocide_engine.logging_config import setup_logging


setup_logging()

parser = argparse.ArgumentParser(description="THE GENOCIDE ENGINE")
parser.add_argument("--version", action="version", version="0.1.0")

args = parser.parse_args()

logging.info("THE GENOCIDE ENGINE started.")