number_terms = {
    "0.125": ["⅛"],
    "0.16666666": ["⅙"],
    "0.2": ["⅕"],
    "0.25": ["¼"],
    "0.3333333": ["⅓"],
    "0.5": ["½"],
    "2.5": ["21/2"],
    "1": ["un", "une"],
    "2": ["deux"],
    "3": ["trois"],
    "4": ["quatre"],
    "5": ["cinq"],
    "6": ["six"],
    "7": ["sept"],
    "8": ["huit"],
    "9": ["neuf"],
    "10": ["dix"],
    "11": ["onze"],
    "12": ["douze"],
    "13": ["treize"],
    "14": ["quatorze"],
    "15": ["quinze"],
    "16": ["seize"],
    "17": ["dix-sept", "dix sept"],
    "18": ["dix-huit", "dix huit"],
    "19": ["dix-neuf", "dix neuf"],
    "20": ["vingt", "vingts"],
    "30": ["trente"],
    "40": ["quarante"],
    "50": ["cinquante"],
    "60": ["soixante"],
    "70": ["soixante dix", "soixante-dix"],
    "80": ["quatre vingt", "quatre-vingt", "quatre vingts", "quatre-vingts"],
    "90": ["quatre vingt dix", "quatre-vingt-dix"],
    "100": ["cent"],
    "500": ["cinq cent", "cinq-cent"],
    "1000": ["mille", "milles"],
}

units_config = {
    # Lengths
    "µm": {
        "dim": "length",
        "degree": 1,
        "scale": 1e-4,
        "terms": [
            "micrometre",
            "micrometres",
            "micro-metre",
            "micrometres",
            "µm",
            "um",
        ],
        "followed_by": None,
    },
    "mm": {
        "dim": "length",
        "degree": 1,
        "scale": 1e-1,
        "terms": ["millimetre", "millimetres", "milimetre", "milimetres", "mm"],
        "followed_by": None,
    },
    "cm": {
        "dim": "length",
        "degree": 1,
        "scale": 1e0,
        "terms": ["centimetre", "centimetres", "cm"],
        "followed_by": None,
    },
    "dm": {
        "dim": "length",
        "degree": 1,
        "scale": 1e1,
        "terms": ["decimetre", "decimetres", "dm"],
        "followed_by": None,
    },
    "m": {
        "dim": "length",
        "degree": 1,
        "scale": 1e2,
        "terms": ["metre", "metres", "m"],
        "followed_by": "cm",
    },
    # Weights
    "µg": {
        "dim": "mass",
        "degree": 1,
        "scale": 1e-1,
        "terms": [
            "microgramme",
            "microgrammes",
            "micro-gramme",
            "microgrammes",
            "µg",
        ],
        "followed_by": None,
    },
    "mg": {
        "dim": "mass",
        "degree": 1,
        "scale": 1e0,
        "terms": [
            "milligramme",
            "miligramme",
            "milligrammes",
            "miligrammes",
            "mgr",
            "mg",
        ],
        "followed_by": None,
    },
    "cg": {
        "dim": "mass",
        "degree": 1,
        "scale": 1e1,
        "terms": ["centigramme", "centigrammes", "cg", "cgr"],
        "followed_by": None,
    },
    "dg": {
        "dim": "mass",
        "degree": 1,
        "scale": 1e2,
        "terms": ["decigramme", "decigrammes", "dgr", "dg"],
        "followed_by": None,
    },
    "g": {
        "dim": "mass",
        "degree": 1,
        "scale": 1e3,
        "terms": ["gramme", "grammes", "gr", "g"],
        "followed_by": None,
    },
    "kg": {
        "dim": "mass",
        "degree": 1,
        "scale": 1e6,
        "terms": ["kilo", "kilogramme", "kilogrammes", "kgr", "kg"],
        "followed_by": "g",
    },
    # Durations
    "second": {
        "dim": "time",
        "degree": 1,
        "scale": 1,
        "terms": ["seconde", "secondes", "s"],
        "followed_by": None,
    },
    "minute": {
        "dim": "time",
        "degree": 1,
        "scale": 60,
        "terms": ["mn", "min", "minute", "minutes"],
        "followed_by": "second",
    },
    "hour": {
        "dim": "time",
        "degree": 1,
        "scale": 3600,
        "terms": ["heure", "heures", "h"],
        "followed_by": "minute",
    },
    "day": {
        "dim": "time",
        "degree": 1,
        "scale": 3600 * 24,
        "terms": ["jour", "jours", "j"],
        "followed_by": None,
    },
    "month": {
        "dim": "time",
        "degree": 1,
        "scale": 3600 * 24 * 30.4167,
        "terms": ["mois"],
        "followed_by": None,
    },
    "week": {
        "dim": "time",
        "degree": 1,
        "scale": 3600 * 24 * 7,
        "terms": ["semaine", "semaines", "sem"],
        "followed_by": None,
    },
    "year": {
        "dim": "time",
        "degree": 1,
        "scale": 3600 * 24 * 365.25,
        "terms": ["an", "année", "ans", "années"],
        "followed_by": None,
    },
    # Angle
    "arc-second": {
        "dim": "time",
        "degree": 1,
        "scale": 2 / 60.0,
        "terms": ['"', "''"],
        "followed_by": None,
    },
    "arc-minute": {
        "dim": "time",
        "degree": 1,
        "scale": 2,
        "terms": ["'"],
        "followed_by": "arc-second",
    },
    "degree": {
        "dim": "time",
        "degree": 1,
        "scale": 120,
        "terms": ["degre", "°", "deg"],
        "followed_by": "arc-minute",
    },
    # Temperature
    "celcius": {
        "dim": "temperature",
        "degree": 1,
        "scale": 1,
        "terms": ["°C", "° celcius", "celcius"],
        "followed_by": None,
    },
    # Volumes
    "ml": {
        "dim": "length",
        "degree": 3,
        "scale": 1e0,
        "terms": ["mililitre", "millilitre", "mililitres", "millilitres", "ml"],
        "followed_by": None,
    },
    "cl": {
        "dim": "length",
        "degree": 3,
        "scale": 1e1,
        "terms": ["centilitre", "centilitres", "cl"],
        "followed_by": None,
    },
    "dl": {
        "dim": "length",
        "degree": 3,
        "scale": 1e2,
        "terms": ["decilitre", "decilitres", "dl"],
        "followed_by": None,
    },
    "l": {
        "dim": "length",
        "degree": 3,
        "scale": 1e3,
        "terms": ["litre", "litres", "l", "dm3"],
        "followed_by": "ml",
    },
    "cac": {
        "dim": "length",
        "degree": 3,
        "scale": 5e-3,
        "terms": ["cac", "c.a.c", "cuillere à café", "cuillères à café"],
        "followed_by": None,
    },
    "goutte": {
        "dim": "length",
        "degree": 3,
        "scale": 5e-5,
        "terms": ["gt", "goutte", "gouttes"],
        "followed_by": None,
    },
    "mm3": {
        "dim": "length",
        "degree": 3,
        "scale": 1e-3,
        "terms": ["mm3", "mm³"],
        "followed_by": None,
    },
    "cm3": {
        "dim": "length",
        "degree": 3,
        "scale": 1e0,
        "terms": ["cm3", "cm³", "cc"],
        "followed_by": None,
    },
    "dm3": {
        "dim": "length",
        "degree": 3,
        "scale": 1e3,
        "terms": ["dm3", "dm³"],
        "followed_by": None,
    },
    "m3": {
        "dim": "length",
        "degree": 3,
        "scale": 1e6,
        "terms": ["m3", "m³"],
        "followed_by": None,
    },
    # Surfaces
    "µm2": {
        "dim": "length",
        "degree": 2,
        "scale": 1e-8,
        "terms": ["µm2", "µm²"],
        "followed_by": None,
    },
    "mm2": {
        "dim": "length",
        "degree": 2,
        "scale": 1e-2,
        "terms": ["mm2", "mm²"],
        "followed_by": None,
    },
    "cm2": {
        "dim": "length",
        "degree": 2,
        "scale": 1e0,
        "terms": ["cm2", "cm²"],
        "followed_by": None,
    },
    "dm2": {
        "dim": "length",
        "degree": 2,
        "scale": 1e2,
        "terms": ["dm2", "dm²"],
        "followed_by": None,
    },
    "m2": {
        "dim": "length",
        "degree": 2,
        "scale": 1e4,
        "terms": ["m2", "m²"],
        "followed_by": None,
    },
    # International units
    "mui": {
        "dim": "ui",
        "degree": 1,
        "scale": 1e0,
        "terms": ["mui", "m ui"],
        "followed_by": None,
    },
    "dui": {
        "dim": "ui",
        "degree": 1,
        "scale": 1e1,
        "terms": ["dui", "d ui"],
        "followed_by": None,
    },
    "cui": {
        "dim": "ui",
        "degree": 1,
        "scale": 1e2,
        "terms": ["cui", "c ui"],
        "followed_by": None,
    },
    "ui": {
        "dim": "ui",
        "degree": 1,
        "scale": 1e3,
        "terms": ["ui"],
        "followed_by": None,
    },
    # Inverse
    "per_µm": {
        "dim": "length",
        "degree": -1,
        "scale": 1e4,
        "terms": ["µm-1"],
        "followed_by": None,
    },
    "per_mm": {
        "dim": "length",
        "degree": -1,
        "scale": 1e1,
        "terms": ["mm-1"],
        "followed_by": None,
    },
    "per_cm": {
        "dim": "length",
        "degree": -1,
        "scale": 1e0,
        "terms": ["cm-1"],
        "followed_by": None,
    },
    "per_dm": {
        "dim": "length",
        "degree": -1,
        "scale": 1e-1,
        "terms": ["dm-1"],
        "followed_by": None,
    },
    "per_m": {
        "dim": "length",
        "degree": -1,
        "scale": 1e-3,
        "terms": ["m-1"],
        "followed_by": None,
    },
    "per_mg": {
        "dim": "mass",
        "degree": -1,
        "scale": 1e-0,
        "terms": ["mgr-1", "mg-1", "mgr⁻¹", "mg⁻¹"],
        "followed_by": None,
    },
    "per_cg": {
        "dim": "mass",
        "degree": -1,
        "scale": 1e-1,
        "terms": ["cg-1", "cgr-1", "cg⁻¹", "cgr⁻¹"],
        "followed_by": None,
    },
    "per_dg": {
        "dim": "mass",
        "degree": -1,
        "scale": 1e-2,
        "terms": ["dgr-1", "dg-1", "dgr⁻¹", "dg⁻¹"],
        "followed_by": None,
    },
    "per_g": {
        "dim": "mass",
        "degree": -1,
        "scale": 1e-3,
        "terms": ["gr-1", "g-1", "gr⁻¹", "g⁻¹"],
        "followed_by": None,
    },
    "per_kg": {
        "dim": "mass",
        "degree": -1,
        "scale": 1e-6,
        "terms": ["kgr-1", "kg-1", "kgr⁻¹", "kg⁻¹"],
        "followed_by": None,
    },
    "per_ml": {
        "dim": "length",
        "degree": -3,
        "scale": 1e-0,
        "terms": ["ml-1", "ml⁻¹"],
        "followed_by": None,
    },
    "per_cl": {
        "dim": "length",
        "degree": -3,
        "scale": 1e-1,
        "terms": ["cl-1", "cl⁻¹"],
        "followed_by": None,
    },
    "per_dl": {
        "dim": "length",
        "degree": -3,
        "scale": 1e-2,
        "terms": ["dl-1", "dl⁻¹"],
        "followed_by": None,
    },
    "per_l": {
        "dim": "length",
        "degree": -3,
        "scale": 1e-3,
        "terms": ["l-1", "l⁻¹"],
        "followed_by": None,
    },
    "per_mm3": {
        "dim": "length",
        "degree": -3,
        "scale": 1e3,
        "terms": ["mm-3", "mm⁻³"],
        "followed_by": None,
    },
    "per_cm3": {
        "dim": "length",
        "degree": -3,
        "scale": 1e-0,
        "terms": ["cm-3", "cm⁻³", "cc-1", "cc⁻¹"],
        "followed_by": None,
    },
    "per_dm3": {
        "dim": "length",
        "degree": -3,
        "scale": 1e-3,
        "terms": ["dm-3", "dm⁻³"],
        "followed_by": None,
    },
    "per_m3": {
        "dim": "length",
        "degree": -3,
        "scale": 1e-6,
        "terms": ["m-3", "m⁻³"],
        "followed_by": None,
    },
    "per_mui": {
        "dim": "ui",
        "degree": -1,
        "scale": 1e-0,
        "terms": ["mui-1", "mui⁻¹"],
        "followed_by": None,
    },
    "per_dui": {
        "dim": "ui",
        "degree": -1,
        "scale": 1e-1,
        "terms": ["dui-1", "dui⁻¹"],
        "followed_by": None,
    },
    "per_cui": {
        "dim": "ui",
        "degree": -1,
        "scale": 1e-2,
        "terms": ["cui-1", "cui⁻¹"],
        "followed_by": None,
    },
    "per_ui": {
        "dim": "ui",
        "degree": -1,
        "scale": 1e-3,
        "terms": ["ui-1", "ui⁻¹"],
        "followed_by": None,
    },
    # Surfaces
    "per_µm2": {
        "dim": "length",
        "degree": -2,
        "scale": 1e8,
        "terms": ["µm-2", "µm⁻²"],
        "followed_by": None,
    },
    "per_mm2": {
        "dim": "length",
        "degree": -2,
        "scale": 1e2,
        "terms": ["mm-2", "mm⁻²"],
        "followed_by": None,
    },
    "per_cm2": {
        "dim": "length",
        "degree": -2,
        "scale": 1e-0,
        "terms": ["cm-2", "cm⁻²"],
        "followed_by": None,
    },
    "per_dm2": {
        "dim": "length",
        "degree": -2,
        "scale": 1e-2,
        "terms": ["dm-2", "dm⁻²"],
        "followed_by": None,
    },
    "per_m2": {
        "dim": "length",
        "degree": -2,
        "scale": 1e-4,
        "terms": ["m-2", "m⁻²"],
        "followed_by": None,
    },
}


common_measurements = {
    "weight": {
        "unit": "kg",
        "unitless_patterns": [
            {
                "terms": ["poids", "poid", "pese", "pesant", "pesait", "pesent"],
                "ranges": [
                    {"min": 0, "max": 200, "unit": "kg"},
                    {"min": 200, "unit": "g"},
                ],
            }
        ],
    },
    "size": {
        "unit": "m",
        "unitless_patterns": [
            {
                "terms": [
                    "mesure",
                    "taille",
                    "mesurant",
                    "mesurent",
                    "mesurait",
                    "mesuree",
                    "hauteur",
                    "largeur",
                    "longueur",
                ],
                "ranges": [
                    {"min": 0, "max": 3, "unit": "m"},
                    {"min": 3, "unit": "cm"},
                ],
            }
        ],
    },
    "bmi": {
        "unit": "kg_per_m2",
        "unitless_patterns": [
            {"terms": ["imc", "bmi"], "ranges": [{"unit": "kg_per_m2"}]}
        ],
    },
    "volume": {"unit": "m3", "unitless_patterns": []},
}

unit_divisors = ["/", "par"]

stopwords = ["par", "sur", "de", "a", ",", "et"]

# Should we only make accented patterns and expect the user to use
# `eds.normalizer` component first ?
range_patterns = [
    ("De", "à"),
    ("De", "a"),
    ("de", "à"),
    ("de", "a"),
    ("Entre", "et"),
    ("entre", "et"),
    (None, "à"),
]
