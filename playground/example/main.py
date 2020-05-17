from example.logging_config import configure_logging
from example.services.pandas_example import PandasExample

logger = configure_logging()

if __name__ == '__main__':
    logger.info("Hello")
    pandas_example = PandasExample
    # pandas_example.read_parquet_with_pyarrow()
    pandas_df = pandas_example.read_parquet_with_wrangler()
    logger.info(pandas_df)
