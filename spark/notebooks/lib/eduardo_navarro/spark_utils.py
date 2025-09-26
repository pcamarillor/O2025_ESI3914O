from urllib.parse import urlparse
from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, ShortType, DoubleType, FloatType,
    BooleanType, DateType, TimestampType, BinaryType,
    ArrayType, MapType
)

class SparkUtils:
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        types_dict = {
            "string": StringType(),
            "int": IntegerType(),
            "short": ShortType(),
            "double": DoubleType(),
            "float": FloatType(),
            "bool": BooleanType(),
            "date": DateType(),
            "time": TimestampType(),
            "binary": BinaryType(),
        }

        fields = []
        for name, type_str in columns_info:
            if type_str not in types_dict:
                raise ValueError(f"Unsupported type: {type_str}")
            fields.append(StructField(name, types_dict[type_str], True))  

        return StructType(fields)
