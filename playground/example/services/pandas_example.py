from pyarrow import fs
import awswrangler as wr


class PandasExample:

    @staticmethod
    def read_parquet_with_pyarrow():
        # https://issues.apache.org/jira/browse/ARROW-8832
        # it does not work :(
        s3 = fs.S3FileSystem(region='eu-west-3')

    @staticmethod
    def read_parquet_with_wrangler():
        # https://issues.apache.org/jira/browse/ARROW-1644
        # it does not work with complex lists in nested structures, so sad :(
        return wr.s3.read_parquet('s3://data-lake-gumartinm/events/wonderful/', dataset=True)
