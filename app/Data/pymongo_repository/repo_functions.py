from bson import ObjectId


def add_model(model_obj, **kwargs):
    obj_temp = model_obj(kwargs)
    obj_temp.save()


def get_all_models(model_obj):
    try:
        return model_obj.all()
    except:
        return None


def get_model_by_id(model_obj, value):
    try:
        return model_obj.find(_id=ObjectId(value)).first_or_none()
    except:
        return None


def get_model_by_column_value(model_obj, column_value, value):
    try:
        return model_obj.find(**{column_value: value}).first_or_none()
    except:
        return None


def get_models_by_column_value(model_obj, column_value, value):
    try:
        return model_obj.find(**{column_value: value})
    except:
        return None


def update_object_by_column(model_obj, column_value, value):
    try:
        return model_obj.update_field(column_value, value)
    except:
        return None


def remove_object(model_obj):
    model_obj.remove_doc()


def get_object_columns(model_obj):
    pass
