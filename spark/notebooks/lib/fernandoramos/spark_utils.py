from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DoubleType, BooleanType, DateType, TimestampType

class SparkUtils:
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        types_dict = {
            "string": StringType(),
            "int": IntegerType(),
            "float": FloatType(),
            "double": DoubleType(),
            "boolean": BooleanType(),
            "date": DateType(),
            "timestamp": TimestampType()
        }
        fields = []

        for col in columns_info:
            name, dtype = col[0], col[1]
            nullable = bool(col[2]) if len(col) > 2 else True  # default to True if not provided
            dtype_key = dtype.lower()
            if dtype_key not in types_dict:
                raise ValueError(f"Unsupported type: {dtype}")
            fields.append(StructField(name, types_dict[dtype_key], nullable))
            
        return StructType(fields)
