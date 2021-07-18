from rest_framework.exceptions import ValidationError

def validate_field_value(data, field):
    try:
        value = data[field]
    except KeyError:
        return data
    else:
        if value is not None and value < 0:
            raise ValidationError(
                "value '{}' must be positive".format(field)
            )
    return data
