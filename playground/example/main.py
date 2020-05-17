from example.logging_config import configure_logging
from example.services.pandas_example import PandasExample

logger = configure_logging()

if __name__ == '__main__':
    logger.info("Testing direct access to S3 with python.")
    pandas_example = PandasExample
    # It does not work :(
    # pandas_example.read_parquet_with_pyarrow()
    wrangler_pandas_df = pandas_example.read_parquet_with_wrangler()
    logger.info(wrangler_pandas_df)
    pandas_df = pandas_example.read_parquet_with_pandas()
    logger.info(pandas_df)
