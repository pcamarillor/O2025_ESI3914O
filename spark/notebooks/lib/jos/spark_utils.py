from dataclasses import fields
from urllib.parse import urlparse
from pyspark.sql.types import StructField, StructType, StringType, IntegerType, ShortType, DoubleType, FloatType, BooleanType, DateType, TimestampType, BinaryType, ArrayType, MapType

def parse_line(line):
    parts = line.strip().split(",")
    return (parts[0], parts[1], parts[2])


def is_yesterday(date_str, yesterday):
    return date_str.split('T', 1)[0] == yesterday


def to_domain(url):
    host = urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host


class SparkUtils:

    types_dict = {
        "string": StringType(),
        "int": IntegerType(),
        "integer": IntegerType(),
        "short": ShortType(),
        "double": DoubleType(),
        "float": FloatType(),
        "boolean": BooleanType(),
        "date": DateType(),
        "timestamp": TimestampType(),
        "binary": BinaryType(),
    }

    @staticmethod
    def generate_schema(columns_info) -> StructType:
        fields = []
        for column_name, column_type in columns_info:
            column_type = column_type.lower()
            if column_type not in SparkUtils.types_dict:
                raise ValueError(f"Unsupported type: {column_type}")
            fields.append(
                StructField(column_name, SparkUtils.types_dict[column_type], True)
            )
        return StructType(fields)
