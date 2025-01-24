import ckan.plugins.toolkit as tk
import ckanext.digitizationknowledge.logic.schema as schema


@tk.side_effect_free
def digitizationknowledge_get_sum(context, data_dict):
    tk.check_access(
        "digitizationknowledge_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.digitizationknowledge_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'digitizationknowledge_get_sum': digitizationknowledge_get_sum,
    }
