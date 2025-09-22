from urllib.parse import urlparse
from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, ShortType, DoubleType, FloatType,
    BooleanType, DateType, TimestampType, BinaryType,
    LongType, ByteType
)

class SparkUtils:
    types_dict = {
        "string": StringType(),
        "int": IntegerType(),
        "long": LongType(),
        "float": FloatType(),
        "double": DoubleType(),
        "boolean": BooleanType(),
        "date": DateType(),
        "timestamp": TimestampType(),
        "binary": BinaryType()
    }

    @staticmethod
    def generate_schema(columns_info) -> StructType:
        return StructType([
            StructField(
                name,
                SparkUtils.types_dict.get(type_str.strip()),
                True   # siempre nullable
            )
            for name, type_str in columns_info
        ])

def parse_line(line: str):
    parts = line.strip().split(",")
    return (parts[0], parts[1], parts[2])

def is_yesterday(date_str: str, yesterday: str) -> bool:
    return date_str.split('T', 1)[0] == yesterday

def to_domain(url: str) -> str:
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host


