from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, BooleanType, LongType, TimestampType

class SparkUtils:
    types_dict = {
        "string": StringType(),
        "int": IntegerType(),
        "integer": IntegerType(),
        "double": DoubleType(),
        "boolean": BooleanType(),
        "long": LongType(),
        "timestamp": TimestampType()
    }

    @staticmethod
    def generate_schema(columns_info) -> StructType:
        """
        Genera un StructType dinámicamente a partir de una lista de tuplas.
        Parámetros:
            columns_info (list): lista de tuplas [(col_name, type_str), ...]
        Retorna:
            StructType con los StructField correspondientes.
        """
        fields = []
        for col_name, col_type in columns_info:
            if col_type.lower() not in SparkUtils.types_dict:
                raise ValueError(f"Tipo '{col_type}' no soportado")
            
            spark_type = SparkUtils.types_dict[col_type.lower()]
            fields.append(StructField(col_name, spark_type, True))  # nullable=True

        return StructType(fields)
