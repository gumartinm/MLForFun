from pandas.logging_config import configure_logging
from pandas.services.pandas_example import PandasExample

logger = configure_logging()

if __name__ == '__main__':
    logger.info("Hello")
    pandas_example = PandasExample
    pandas_example.read_parquet()
