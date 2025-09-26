from urllib.parse import urlparse
from pyspark.sql.types import StructField, StructType, StringType, IntegerType, ShortType, DoubleType, FloatType, BooleanType, DateType, TimestampType, BinaryType, ArrayType, MapType

types_dict = {
    "string": StringType(),
    "struct": StructType(),
    "int": IntegerType(),
    "short": ShortType(),
    "double": DoubleType(),
    "float": FloatType(),
    "bool": BooleanType(),
    "date": DateType(),
    "time": TimestampType(),
    "binary": BinaryType(),
    "array_int": ArrayType(IntegerType()),
    "map": MapType(StringType(), IntegerType())

}


class SparkUtils:
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        schema_fields = []
        for col_name, col_type in columns_info:
            if col_type in types_dict: 
                typeFromDict = types_dict[col_type.lower()]
                field = StructField(col_name, typeFromDict,True)
                schema_fields.append(field)
            else:
                raise NotImplementedError("Not implemented yet")
        return StructType(schema_fields)
