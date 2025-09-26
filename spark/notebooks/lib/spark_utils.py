from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType,
    FloatType, DoubleType, BooleanType, DateType, TimestampType
)
from typing import List, Tuple


class SchemaGenerator:
    def __init__(self):
        #Diccionario de mapeo de tipos soportados
        self.type_mapping = {
            'StringType': StringType,
            'IntegerType': IntegerType,
            'FloatType': FloatType,
            'DoubleType': DoubleType,
            'BooleanType': BooleanType,
            'DateType': DateType,
            'TimestampType': TimestampType
        }

    def generate_schema(self, columns: List[Tuple[str, str]]) -> StructType:
        fields = []
        for col_name, col_type in columns:
            if col_type in self.type_mapping:
                fields.append(StructField(col_name, self.type_mapping[col_type](), True))
            else:
                raise ValueError(f"Tipo de dato no soportado: {col_type}")
        return StructType(fields)
