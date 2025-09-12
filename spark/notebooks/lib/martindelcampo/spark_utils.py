from typing import Iterable, Tuple, Union
import re
from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, ShortType, LongType, ByteType,
    DoubleType, FloatType, BooleanType, DateType, TimestampType,
    BinaryType, DecimalType, ArrayType, MapType, DataType
)

class SparkUtils:
    types_dictionary = {
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
        "long": LongType(),
        "byte": ByteType(),
        "decimal": DecimalType(10, 0), 
        "array": ArrayType(StringType()),  
        "map": MapType(StringType(), StringType()),
        "dataframe": DataType()
        }

    def generate_schema(columns_info) -> StructType:
        fields = []
        for col_name, col_type in columns_info:
            dtype = SparkUtils.types_dictionary.get(col_type.lower())
            if not dtype:
                raise ValueError(f"Unsupported type: {col_type}")
            fields.append(StructField(col_name, dtype, True))
        return StructType(fields)