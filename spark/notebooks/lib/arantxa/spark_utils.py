from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, FloatType, BooleanType, DateType, TimestampType, LongType, ShortType, ByteType

class SparkUtils:
    
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        """
        Generate a StructType schema from a list of tuples.
        
        Args:
            columns_info (list): List of tuples where each tuple contains 
                                (column_name, type_string) where type_string
                                is a simple string like "string", "int", "double", etc.
        
        Returns:
            StructType: The generated schema
        
        Example:
            schema = SparkUtils.generate_schema([("name", "string"), ("age", "int")])
        """
        # Mapping of simple type names to PySpark types
        type_mapping = {
            "string": StringType(),
            "str": StringType(),
            "int": IntegerType(),
            "integer": IntegerType(),
            "double": DoubleType(),
            "float": FloatType(),
            "boolean": BooleanType(),
            "bool": BooleanType(),
            "date": DateType(),
            "timestamp": TimestampType(),
            "long": LongType(),
            "short": ShortType(),
            "byte": ByteType()
        }
        
        struct_fields = []
        
        for column_name, type_string in columns_info:
            # Convert to lowercase for case-insensitive matching
            type_lower = type_string.lower()
            
            if type_lower not in type_mapping:
                raise ValueError(f"Unsupported type: {type_string}. Supported types are: {list(type_mapping.keys())}")
            
            spark_type = type_mapping[type_lower]
            struct_field = StructField(column_name, spark_type, True)  # nullable=True
            struct_fields.append(struct_field)
        
        return StructType(struct_fields)