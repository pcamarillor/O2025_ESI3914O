from pyspark.sql.types import (
    StructType, 
    StructField, 
    StringType, 
    IntegerType, 
    ShortType, 
    DoubleType, 
    FloatType, 
    BooleanType, 
    DateType, 
    TimestampType, 
    BinaryType, 
    ArrayType, 
    MapType
)

class SparkUtils:
    # Dictionary mapping string representations to Spark data types.
    # This handles various common naming conventions (e.g., "string", "StringType", "str").
    _TYPES_DICT = {
        "stringtype": StringType(),
        "integertype": IntegerType(),
        "shorttype": ShortType(),
        "doubletype": DoubleType(),
        "floattype": FloatType(),
        "booleantype": BooleanType(),
        "datetype": DateType(),
        "timestamptype": TimestampType(),
        "binarytype": BinaryType(),
    }

    @staticmethod
    def generate_schema(columns_info: list[tuple[str, str]]) -> StructType:
        schema = StructType()
        for col_name, col_type_str in columns_info:
            # Normalize the type string to lower case to match dictionary keys
            normalized_type_str = col_type_str.lower()
            
            # Look up the corresponding Spark type object from the dictionary
            spark_type = SparkUtils._TYPES_DICT.get(normalized_type_str)
            
            if spark_type is None:
                raise ValueError(
                    f"Unsupported data type '{col_type_str}'. "
                    f"Supported types are: {list(SparkUtils._TYPES_DICT.keys())}"
                )
            
            # Use the add method, which creates and adds the StructField internally
            schema = schema.add(col_name, spark_type, True)
            
        return schema