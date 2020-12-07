from bson import ObjectId


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


def get_models_by_column_value(model_obj, column_value, value):
    pass


def update_object_by_column(model_obj, column_value, value):
    return model_obj.update_field(column_value, value)


def remove_object(model_obj):
    pass
