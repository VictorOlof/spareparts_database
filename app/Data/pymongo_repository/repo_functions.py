from bson import ObjectId


def add_model(model_obj, **kwargs):
    obj_temp = model_obj(kwargs)
    obj_temp.save()
    return obj_temp


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


def insert_items_to_embedded_list(model_obj, obj_id: str, list_name: str, value: dict):
    model_obj.insert_to_embedded_list(ObjectId(obj_id), list_name, value)


def insert_items_to_embedded_field(model_obj, obj_id: str, field_name: str, value: dict):
    model_obj.insert_to_embedded_field(ObjectId(obj_id), field_name, value)


def create_items_from_embedded_list(model_obj, obj_id, list_name, create_obj):
    try:
        obj_temp = get_model_by_id(model_obj, obj_id)
        result = []
        for item in getattr(obj_temp, list_name):
            obj_temp_2 = create_obj(item)
            obj_temp_2._id = obj_id
            result.append(obj_temp_2)
            print(obj_temp_2)
        return result
    except:
        return None


def create_item_from_embedded_field(model_obj, obj_id, list_name, create_obj):
    try:
        obj_temp = get_model_by_id(model_obj, obj_id)
        obj_data = getattr(obj_temp, list_name)
        obj_temp_2 = create_obj(obj_data)
        obj_temp_2._id = obj_id
        return obj_temp_2
    except:
        return None
