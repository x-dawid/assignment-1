def kelvin(temperature,to_kelvin=True):
    
        if to_kelvin: 
            temperature = round(temperature + 273.3)
        else:
            temperature = round(temperature - 273.3)
        return temperature  




