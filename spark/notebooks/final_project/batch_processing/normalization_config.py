# Brand aliases - normalize brand variations to canonical form
BRAND_ALIASES = {
    # Hyphen/space variations
    "MERCEDES-BENZ": "MERCEDES BENZ",
    "LAND-ROVER": "LAND ROVER",
    "BMW-ALPINA": "BMW ALPINA",

    # Suffix removal (from Qualitas BRAND_CONSOLIDATION_MAP)
    "BMW BW": "BMW",
    "VOLKSWAGEN VW": "VOLKSWAGEN",
    "CHEVROLET GM": "CHEVROLET",
    "FORD FR": "FORD",
    "AUDI II": "AUDI",

    # Variant consolidation
    "KIA MOTORS": "KIA",
    "TESLA MOTORS": "TESLA",
    "MERCEDES BENZ II": "MERCEDES BENZ",
    "NISSAN II": "NISSAN",
    "GREAT WALL MOTORS": "GREAT WALL",

    # MINI handling - IMPORTANT: Keep MINI separate, don't merge with BMW
    "BMW MINI": "MINI",
    "MINI COOPER": "MINI",

    # General Motors variants
    "GENERAL MOTORS": "GMC",
    "GENERAL MOTORS 2": "GMC",
    "GENERAL MOTORS COMPANY": "GMC",
    "GENERAL MOTORS CORPORATION": "GMC",

    # Other variants
    "JAC SEI": "JAC",
    "MG ROVER": "MG",

    # Typo corrections
    "BERCEDES": "MERCEDES BENZ",
    "BUIK": "BUICK",
}

# Model aliases - normalize model variations
# These handle common model name inconsistencies across insurers
MODEL_ALIASES = {
    # BMW: Remove "SERIE" prefix (applied after brand normalization)
    # Example: "SERIE 3" → "3", "SERIE 1" → "1"
    # NOTE: This is handled in normalize_brand_model UDF with regex pattern

    # BMW: Fix trim spacing (handled in UDF)
    # Example: "118 I" → "118I", "120 IA" → "120IA"

    # Mercedes-Benz: Class name variations
    "CLASE A": "A-CLASS",
    "CLASE C": "C-CLASS",
    "CLASE E": "E-CLASS",
    "CLASE G": "G-CLASS",
    "CLASE S": "S-CLASS",
    "CLASE CLA": "CLA-CLASS",
    "CLASE CLS": "CLS-CLASS",
    "CLASE GLA": "GLA-CLASS",
    "CLASE GLB": "GLB-CLASS",
    "CLASE GLC": "GLC-CLASS",
    "CLASE GLE": "GLE-CLASS",
    "CLASE GLS": "GLS-CLASS",
    "A CLASS": "A-CLASS",
    "C CLASS": "C-CLASS",
    "E CLASS": "E-CLASS",
    "G CLASS": "G-CLASS",
    "S CLASS": "S-CLASS",

    # Volkswagen: VW prefix removal
    "VW GOLF": "GOLF",
    "VW JETTA": "JETTA",
    "VW TIGUAN": "TIGUAN",
    "VW POLO": "POLO",

    # Hyphen variations
    "T CROSS": "T-CROSS",
    "TCROSS": "T-CROSS",
    "X TRAIL": "X-TRAIL",
    "XTRAIL": "X-TRAIL",

    # Common abbreviations
    "WRANGLER JK": "WRANGLER",
    "WRANGLER JL": "WRANGLER",
    "WRANGLER TJ": "WRANGLER",

    # Number format variations
    "F 150": "F-150",
    "F150": "F-150",
    "RAM 1500": "1500",
    "RAM 2500": "2500",
    "RAM 3500": "3500",
}

# Specs to remove from MODELO field (these belong in VERSION, not MODEL)
# From MODELO_SPECS_TO_REMOVE in all insurer JS files
MODEL_SPECS_TO_REMOVE = [
    "VAN", "WAGON", "SEDAN", "HATCHBACK", "HATCH BACK",
    "COUPE", "CONVERTIBLE", "SUV", "CROSSOVER", "CROSS COUNTRY",
    "PICK UP", "PICKUP",
    "RS", "GT", "GTI", "GTS", "AMG", "SRT", "S-LINE", "M-SPORT",
    "TYPE-R", "TYPE-S", "A-SPEC", "NISMO", "TRD",
    "CROSS", "SPORT", "LUXURY", "LIMITED", "EXECUTIVE", "PREMIUM",
    "DERBY", "NUEVO", "NUEVA", "NEW", "JOYLONG",
    "EDITION", "SPECIAL", "ANNIVERSARY",
    # BMW-specific: SDRIVE/XDRIVE should be in version, not model
    "SDRIVE", "XDRIVE",
]

# Token exclusion list - irrelevant comfort/audio/safety tokens to exclude from matching
# Based on ZURICH_NORMALIZATION_DICTIONARY.irrelevant_comfort_audio from reference
TOKEN_EXCLUSIONS = [
    # Audio/Navigation
    "AA", "EE", "CD", "DVD", "GPS", "BT", "USB", "MP3", "AM", "RA", "FX",
    "BOSE", "HARMAN KARDON", "HARMAN/KARDON", "BEATS", "JBL", "ALPINE", "SONY",
    "SIS/NAV", "SIS.NAV.", "SIS NAV", "SIS.NAVEGACION", "SIST.NAV", "SIST NAV",
    "PAQ.NAVEG", "PAQ NAVEG", "PAQ.NAVEGACION", "PAQ NAV",
    "NAVEGACION", "NAVEG", "NAV.", "NAV", "NAVI", "NAVIGATOR",
    "RCD", "RNS", "MIB", "MMI", "REPRODUCTOR", "PANTALLA",
    "TOUCH SCREEN", "TOUCHSCREEN", "DISPLAY", "MONITOR",
    "BLUETOOTH", "AUX", "RADIO", "STEREO", "ESTEREO",
    "SOUND SYSTEM", "SISTEMA AUDIO", "AUDIO PREMIUM",

    # Comfort features
    "PIEL", "CUERO", "LEATHER", "TELA", "ALCANTARA", "GAMUZA", "VINYL",
    "ASIENTOS ELECTRICOS", "ASIENTOS ELECT",
    "QUEMACOCOS", "TECHO SOLAR", "SUNROOF", "PANORAMIC", "PANORAMICO",
    "CLIMATIZADOR", "CLIMA DUAL", "BI-ZONA", "BIZONA",
    "CALEFACCION", "VENTILACION",
    "ASIENTOS CALEFACTABLES", "ASIENTO GIRATORIO",

    # Safety (abbreviations)
    "BA", "ABS", "QC", "Q/C", "Q.C.", "VP", "V/P",
    "CA", "C/A", "A/C", "AC", "CE", "SQ", "CB", "CQ", "SM", "VT",
    "EBD", "ESP", "VSC", "TCS",

    # Tire sizes
    "R13", "R14", "R15", "R16", "R17", "R18", "R19", "R20", "R21", "R22",

    # Generic modifiers
    "NUEVO", "NEW", "NUEVA",
]

# Transmission inference keywords - used when transmision field is empty
# Maps transmission-related keywords found in version_original to AUTO/MANUAL
TRANSMISSION_KEYWORDS = {
    # Automatic indicators
    "AUT": "AUTO",
    "AUTO": "AUTO",
    "AUTOMATICA": "AUTO",
    "AUTOMATIC": "AUTO",
    "AUTOMÁTICO": "AUTO",
    "CVT": "AUTO",
    "AT": "AUTO",
    "A/T": "AUTO",
    "DSG": "AUTO",
    "TIPTRONIC": "AUTO",
    "MULTITRONIC": "AUTO",
    "POWERSHIFT": "AUTO",
    "DUAL CLUTCH": "AUTO",

    # Manual indicators
    "MAN": "MANUAL",
    "MANUAL": "MANUAL",
    "MT": "MANUAL",
    "M/T": "MANUAL",
    "STD": "MANUAL",
    "STANDARD": "MANUAL",
    "ESTANDAR": "MANUAL",
    "ESTÁNDAR": "MANUAL",
}

# Unit standardization - normalize measurement units
UNIT_MAPPINGS = {
    # Horsepower
    "CP": "HP",
    "CV": "HP",
    "PS": "HP",
    "H": "HP",

    # Liters
    "LTS": "L",
    "LTR": "L",
    "LITROS": "L",
    "LITER": "L",
    "LITERS": "L",

    # Cylinders
    "CYL": "CIL",
    "CILINDROS": "CIL",
    "CYLINDER": "CIL",
    "CYLINDERS": "CIL",
}

# Synonym mappings - normalize token variants to canonical form
# Based on normalize_token function from funciones-homologacion-v2.13.0.sql
SYNONYM_MAPPINGS = {
    # Body types
    "SED": "SEDAN",
    "SEDÁN": "SEDAN",
    "CP": "COUPE",
    "COUPÉ": "COUPE",
    "SW": "WAGON",
    "STATION": "WAGON",
    "STATIONWAGON": "WAGON",
    "MINIVAN": "VAN",
    "MINIVÁN": "VAN",
    "CABRIO": "CONVERTIBLE",
    "CABRIOLET": "CONVERTIBLE",
    "DESCAPOTABLE": "CONVERTIBLE",
    "HB": "HATCHBACK",
    "HATCH": "HATCHBACK",
    "PICKUP": "PICKUP",
    "PICK-UP": "PICKUP",
    "PU": "PICKUP",
    "CROSSOVER": "SUV",

    # Drivetrain
    "4X4": "AWD",
    "4X2": "2WD",
    "4WD": "AWD",
    "ALLWHEELDRIVE": "AWD",
    "TRACCIÓN INTEGRAL": "AWD",
    "TRACCION INTEGRAL": "AWD",
    "DELANTERA": "FWD",
    "TRACCIÓN DELANTERA": "FWD",
    "TRACCION DELANTERA": "FWD",
    "TRASERA": "RWD",
    "TRACCIÓN TRASERA": "RWD",
    "TRACCION TRASERA": "RWD",
    "2X4": "2WD",

    # Powertrains
    "ELECTRIC": "ELECTRIC",
    "ELECTRICO": "ELECTRIC",
    "ELÉCTRICO": "ELECTRIC",
    "EV": "ELECTRIC",
    "BEV": "ELECTRIC",
    "HYBRID": "HYBRID",
    "HIBRIDO": "HYBRID",
    "HÍBRIDO": "HYBRID",
    "HEV": "HYBRID",
    "HYBRIDE": "HYBRID",
    "PHEV": "PHEV",
    "PLUG-IN": "PHEV",
    "PLUGIN": "PHEV",
    "MHEV": "MHEV",
    "MILD": "MHEV",
    "MILDHYBRID": "MHEV",
    "DSL": "DIESEL",
    "DIÉSEL": "DIESEL",
    "GASOLINE": "GASOLINA",
    "GAS": "GASOLINA",
    "PETROL": "GASOLINA",
    "NAFTA": "GASOLINA",
    "GNV": "GNV",
    "GNC": "GNV",
    "CNG": "GNV",
    "GLP": "GLP",
    "LPG": "GLP",

    # Doors
    "2PTAS": "2PUERTAS",
    "2P": "2PUERTAS",
    "2-PUERTAS": "2PUERTAS",
    "2 PUERTAS": "2PUERTAS",
    "3PTAS": "3PUERTAS",
    "3P": "3PUERTAS",
    "3-PUERTAS": "3PUERTAS",
    "3 PUERTAS": "3PUERTAS",
    "4PTAS": "4PUERTAS",
    "4P": "4PUERTAS",
    "4-PUERTAS": "4PUERTAS",
    "4 PUERTAS": "4PUERTAS",
    "5PTAS": "5PUERTAS",
    "5P": "5PUERTAS",
    "5-PUERTAS": "5PUERTAS",
    "5 PUERTAS": "5PUERTAS",

    # Occupants
    "2OCUP": "2OCUP",
    "2 OCUP": "2OCUP",
    "2OCUPANTES": "2OCUP",
    "2 OCUPANTES": "2OCUP",
    "3OCUP": "3OCUP",
    "3 OCUP": "3OCUP",
    "3OCUPANTES": "3OCUP",
    "3 OCUPANTES": "3OCUP",
    "03 OCUP": "3OCUP",
    "03OCUP": "3OCUP",
    "4OCUP": "4OCUP",
    "4 OCUP": "4OCUP",
    "4OCUPANTES": "4OCUP",
    "4 OCUPANTES": "4OCUP",
    "04 OCUP": "4OCUP",
    "04OCUP": "4OCUP",
    "5OCUP": "5OCUP",
    "5 OCUP": "5OCUP",
    "5OCUPANTES": "5OCUP",
    "5 OCUPANTES": "5OCUP",
    "05 OCUP": "5OCUP",
    "05OCUP": "5OCUP",
    "6OCUP": "6OCUP",
    "6 OCUP": "6OCUP",
    "6OCUPANTES": "6OCUP",
    "6 OCUPANTES": "6OCUP",
    "06 OCUP": "6OCUP",
    "06OCUP": "6OCUP",
    "7OCUP": "7OCUP",
    "7 OCUP": "7OCUP",
    "7OCUPANTES": "7OCUP",
    "7 OCUPANTES": "7OCUP",
    "07 OCUP": "7OCUP",
    "07OCUP": "7OCUP",
    "8OCUP": "8OCUP",
    "8 OCUP": "8OCUP",
    "8OCUPANTES": "8OCUP",
    "8 OCUPANTES": "8OCUP",
    "08 OCUP": "8OCUP",
    "08OCUP": "8OCUP",
    "9OCUP": "9OCUP",
    "9 OCUP": "9OCUP",
    "9OCUPANTES": "9OCUP",
    "9 OCUPANTES": "9OCUP",
    "09 OCUP": "9OCUP",
    "09OCUP": "9OCUP",

    # Cylinders
    "3 CIL": "3CIL",
    "L3": "3CIL",
    "3-CIL": "3CIL",
    "4 CIL": "4CIL",
    "L4": "4CIL",
    "4-CIL": "4CIL",
    "I4": "4CIL",
    "5 CIL": "5CIL",
    "L5": "5CIL",
    "5-CIL": "5CIL",
    "6 CIL": "6CIL",
    "V6": "6CIL",
    "6-CIL": "6CIL",
    "L6": "6CIL",
    "H6": "6CIL",
    "8 CIL": "8CIL",
    "V8": "8CIL",
    "8-CIL": "8CIL",
    "10 CIL": "10CIL",
    "V10": "10CIL",
    "10-CIL": "10CIL",
    "12 CIL": "12CIL",
    "V12": "12CIL",
    "W12": "12CIL",
    "12-CIL": "12CIL",

    # Trim levels
    "EXECUTIVE": "PREMIUM",
    "EXCLUSIVO": "PREMIUM",
    "EXCLUSIVE": "PREMIUM",
    "EJECUTIVO": "PREMIUM",
    "LUXURY": "LUJO",
    "LUJO": "LUJO",
    "LUX": "LUJO",
    "TECHNOLOGY": "TECH",
    "TECNOLOGIA": "TECH",
    "SPORTLINE": "SPORT",
    "SLINE": "SPORT",
    "DEPORTIVO": "SPORT",
    "BITURBO": "TURBO",
    "BITBO": "TURBO",
    "TWINTURBO": "TURBO",
    "LIMITED EDITION": "LIMITED",
    "EDITION": "LIMITED",
    "EDICION": "LIMITED",
    "EDICIÓN": "LIMITED",
    "ADVANCED": "ADVANCE",
    "AVANZADO": "ADVANCE",
    "AVANCE": "ADVANCE",
    "CONFORT": "COMFORT",
    "COMFORTLINE": "COMFORT",
    "CONFORTLINE": "COMFORT",
    "DINAMICO": "DYNAMIC",
    "DINÁMICO": "DYNAMIC",
    "DYNAMIQUE": "DYNAMIC",
    "HIGHLINE": "HIGHLINE",
    "HIGLINE": "HIGHLINE",
    "ELEGANCIA": "ELEGANCE",
    "ELEGANT": "ELEGANCE",
    "ELEGANTE": "ELEGANCE",
    "PRESTIGIO": "PRESTIGE",
    "PRESTIGIOUS": "PRESTIGE",
}

# Tokens to completely remove (return None in normalization)
TOKENS_TO_REMOVE = [
    "XL", "PLUS", "L", "BASE", "BASICO", "BÁSICO",
    "PACK", "PACKAGE", "PAQUETE",
]

# Hyphen exception list - tokens with hyphens that should be normalized (not preserved)
# From SQL BUGFIX v2.11.3.1
HYPHEN_EXCEPTIONS = [
    "PICK-UP",  # → PICKUP
    "PLUG-IN",  # → PHEV
]
