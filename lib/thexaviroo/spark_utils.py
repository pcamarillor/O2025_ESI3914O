from pyspark.sql.types import StructType, StructField, StringType, IntegerType

class SparkUtils:
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        type_mapping = {
        "string": StringType(),
        "int": IntegerType(),
        "float": FloatType(),
        "boolean": BooleanType(),
        "timestamp": TimestampType(),
        "date": DateType(),
        "long": LongType(),
        }


        fields = [
            StructField(name, type_mapping[data_type], True)
            for name, data_type in columns_info
        ]

        return StructType(fields)
