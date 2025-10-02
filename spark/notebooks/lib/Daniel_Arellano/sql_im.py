"""Imports."""
from pyspark.sql.types import (  # type: ignore
    ArrayType,  # noqa: F401
    BinaryType,  # noqa: F401
    BooleanType,  # noqa: F401
    DateType,  # noqa: F401
    DoubleType,  # noqa: F401
    FloatType,  # noqa: F401
    IntegerType,  # noqa: F401
    LongType,
    MapType,  # noqa: F401
    ShortType,  # noqa: F401
    StringType,  # noqa: F401
    StructField,
    StructType,
    TimestampType,  # noqa: F401
    ArrayType,
)

types = {
            "string": StringType(),
            "int": IntegerType(),
            "long": LongType(),
            "short": ShortType(),
            "double": DoubleType(),
            "float": FloatType(),
            "boolean": BooleanType(),
            "date": DateType(),
            "timestamp": TimestampType(),
            "binary": BinaryType(),
            "array_int": ArrayType(IntegerType()),
            "struct": StructType()
}


class SparkUtils:
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        # Creamos una lista de (nombre, tipo, nullable)
        fields = []
        for name, dtype in columns_info:
            spark_type = types[dtype.lower()]  # busca el tipo en el dict
            field = StructField(name, spark_type, True)  # nullable = True por defecto
            # print(f"Nombre: {field.name}, Tipo: {field.dataType}, Nullable: {field.nullable}")
            fields.append(field)
        return StructType(fields)
