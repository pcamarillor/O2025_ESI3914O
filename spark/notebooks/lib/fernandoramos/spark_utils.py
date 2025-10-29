from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DoubleType, BooleanType, DateType, TimestampType, ArrayType

class SparkUtils:
    @staticmethod
    def generate_schema(columns_info) -> StructType:
        fields = []

        for col in columns_info:
            name = col[0]
            dtype_str = col[1]
            nullable = bool(col[2]) if len(col) > 2 else True

            # Parse the type string and create appropriate Spark type
            spark_type = SparkUtils._parse_type(dtype_str)
            fields.append(StructField(name, spark_type, nullable))

        return StructType(fields)

    @staticmethod
    def _parse_type(type_str: str):
        type_str = type_str.strip()

        # Simple types
        simple_types = {
            "string": StringType(),
            "int": IntegerType(),
            "integer": IntegerType(),
            "float": FloatType(),
            "double": DoubleType(),
            "boolean": BooleanType(),
            "bool": BooleanType(),
            "date": DateType(),
            "timestamp": TimestampType()
        }

        if type_str.lower() in simple_types:
            return simple_types[type_str.lower()]

        # Array types: array<element_type>
        if type_str.startswith("array<") and type_str.endswith(">"):
            element_type_str = type_str[6:-1]  # Extract content between "array<" and ">"
            element_type = SparkUtils._parse_type(element_type_str)
            return ArrayType(element_type, containsNull=False)

        # Struct types: struct<field1:type1,field2:type2>
        if type_str.startswith("struct<") and type_str.endswith(">"):
            fields_str = type_str[7:-1]  # Extract content between "struct<" and ">"
            struct_fields = SparkUtils._parse_struct_fields(fields_str)
            return StructType(struct_fields)

        raise ValueError(f"Unsupported type: {type_str}")

    @staticmethod
    def _parse_struct_fields(fields_str: str):
        fields = []
        current_field = ""
        depth = 0  # Track nesting level for angle brackets

        # Split by commas, but respect nested angle brackets
        for char in fields_str:
            if char in ('<', '{'):
                depth += 1
            elif char in ('>', '}'):
                depth -= 1

            if char == ',' and depth == 0:
                # End of current field
                if current_field.strip():
                    fields.append(SparkUtils._parse_struct_field(current_field.strip()))
                current_field = ""
            else:
                current_field += char

        if current_field.strip():
            fields.append(SparkUtils._parse_struct_field(current_field.strip()))

        return fields

    @staticmethod
    def _parse_struct_field(field_def: str):
        # Split on first colon only (type definition may contain colons)
        parts = field_def.split(':', 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid struct field definition: {field_def}")

        field_name = parts[0].strip()
        field_type_str = parts[1].strip()

        field_type = SparkUtils._parse_type(field_type_str)
        return StructField(field_name, field_type, nullable=False)
