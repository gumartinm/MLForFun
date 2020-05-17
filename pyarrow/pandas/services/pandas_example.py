from pyarrow import fs


class PandasExample:

    @staticmethod
    def read_parquet():
        s3 = fs.S3FileSystem(region='eu-west-3')

