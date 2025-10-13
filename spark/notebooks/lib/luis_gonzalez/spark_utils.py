from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType, BooleanType, 
    DoubleType, TimestampType, FloatType
)

class SparkUtils:
    """A helper class for Spark."""
    _type_lookup = {
        "string": StringType(),
        "int": IntegerType(),
        "bool": BooleanType(),
        "double": DoubleType(),
        "float": FloatType(),
        "time": TimestampType(),
        "time": TimestampType(),
        "float": FloatType(),
    }

    @staticmethod
    def generate_schema(columns: list[tuple[str, str]]) -> StructType:
        fields = []
        
        for col_name, col_type_text in columns:
            
            spark_type = SparkUtils._type_lookup.get(col_type_text)
            
            if spark_type is None:
                raise ValueError(f"Sorry, I don't know the type '{col_type_text}'!")

            rule = StructField(col_name, spark_type, True)
            fields.append(rule)
            
        return StructType(fields)