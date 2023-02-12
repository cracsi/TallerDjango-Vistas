from ..models import Measurement


def get_measurements():
    measurements=Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def delete_measurement(var_pk):
    # measurement = Measurement.objects.get(pk=var_pk)
    Measurement.objects.delete(pk=var_pk)
    return ""

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.variable = new_var["variable"]
    measurement.value= new_var["value"]
    measurement.unit= new_var["unit"]
    measurement.place= new_var["place"]
    measurement.dateTime= new_var["dateTime"]
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(variable=var["variable"], value=var["value"], unit=var["unit"], place=var["place"], dateTime=var["dateTime"])
    measurement.save()
    return measurement

