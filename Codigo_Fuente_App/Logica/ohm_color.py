def get_tolerance(**value: str) -> dict:
    tolerances = [
        {"color": "brown", "percentage": 1, "number": 1},
        {"color": "red", "percentage": 2, "number": 2},
        {"color": "green", "percentage": 0.5, "number": 5},
        {"color": "blue", "percentage": 0.25, "number": 6},
        {"color": "violet", "percentage": 0.1, "number": 7},
        {"color": "gray", "percentage": 0.05, "number": 8},
        {"color": "gold", "percentage": 5, "number": 10},
        {"color": "silver", "percentage": 10, "number": 11},
    ]
    
    if value.get("color"):
        for tolerance in tolerances:
            if tolerance.get("color") == value.get("color"):
                return tolerance

    if value.get("number"):
        for tolerance in tolerances:
            if tolerance.get("number") == value.get("number"):
                return tolerance

    return None

def get_band(**value) -> dict:
    bands = [
        {"color": "black", "number": 0, "multiplier": 1},
        {"color": "brown", "number": 1, "multiplier": 10},
        {"color": "red", "number": 2, "multiplier": 100},
        {"color": "orange", "number": 3, "multiplier": 1000},
        {"color": "yellow", "number": 4, "multiplier": 10000},
        {"color": "green", "number": 5, "multiplier": 100000},
        {"color": "blue", "number": 6, "multiplier": 1000000},
        {"color": "violet", "number": 7, "multiplier": 10000000},
        {"color": "gray", "number": 8, "multiplier": 100000000},
        {"color": "white", "number": 9, "multiplier": 1000000000},
        {"color": "gold", "number": 10, "multiplier": 0.1},
        {"color": "silver", "number": 11, "multiplier": 0.01}
    ]
    if value.get("color"):
        for band in bands:
            if band.get("color") == value.get("color"):
                return band
    if value.get("number") >= 0 and value.get("number") <= 11:
        for band in bands:
            if band.get("number") == value.get("number"):
                return band
    return None

def get_value(
    band_1_num=-1,
    band_2_num=-1,
    multiplier_num=-1,
    band_1_name="",
    band_2_name="",
    multiplier_name=-1,
    
    ) -> float:

    if band_1_num > -1 and band_2_num > -1 and multiplier_num > -1:
        value_1 = get_band(number=band_1_num)["number"]
        value_2 = get_band(number=band_2_num)["number"]
        multiplier = get_band(number=multiplier_num)["multiplier"]
        
        value_base = int(f"{value_1}{value_2}")
        return value_base * multiplier
    elif band_1_name and band_2_name and multiplier_name:
        value_1 = get_band(color=band_1_name)["number"]
        value_2 = get_band(color=band_2_name)["number"]
        multiplier = get_band(color=multiplier_name)["multiplier"]
        value_base = int(f"{value_1}{value_2}")
        return value_base * multiplier
    
    return None

def get_range_tolerance(value: float, tolerance: str):
    
    value_tolerance = get_tolerance(color=tolerance)["percentage"]
    value_down = value - ((value * value_tolerance) / 100)
    value_up = value + ((value * value_tolerance) / 100)
    return (value_down, value_up)
    
def main():
    valor = get_value(band_1_num=2, band_2_num=3, multiplier_num=4)
    print(valor)
    print(get_range_tolerance(valor, "gold"))
    print("=====================")
    valor = get_value(band_1_name="red", band_2_name="orange", multiplier_name="yellow")
    print(valor)
    
if __name__ == "__main__":
    main()
