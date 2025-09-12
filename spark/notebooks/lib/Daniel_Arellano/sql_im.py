"""Imports."""
from pyspark.sql.types import (  # type: ignore
    ArrayType,  # noqa: F401
    BinaryType,  # noqa: F401
    BooleanType,  # noqa: F401
    DateType,  # noqa: F401
    DoubleType,  # noqa: F401
    FloatType,  # noqa: F401
    IntegerType,  # noqa: F401
    MapType,  # noqa: F401
    ShortType,  # noqa: F401
    StringType,  # noqa: F401
    StructType,
    TimestampType,  # noqa: F401
    StructField
)

types = {
    "ArrayType": ArrayType(StringType()),  # Default: array de strings
    "MapType": MapType(StringType(), StringType()),  # Default: map de string->string
    "BinaryType": BinaryType(),
    "BooleanType": BooleanType(),
    "DateType": DateType(),
    "DoubleType": DoubleType(),
    "FloatType": FloatType(),
    "int": IntegerType(),
    "ShortType": ShortType(),
    "string": StringType(),
    "TimestampType": TimestampType(),
}


class SparkUtils:
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        # Creamos una lista de (nombre, tipo, nullable)
        fields = []
        for name, dtype in columns_info:
            spark_type = types[dtype.lower()]  # busca el tipo en el dict
            field = StructField(name, spark_type, True)  # nullable = True por defecto
            #print(f"Nombre: {field.name}, Tipo: {field.dataType}, Nullable: {field.nullable}")
            fields.append(field)
        return StructType(fields)
