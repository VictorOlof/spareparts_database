from Data.db import session


def add_model(model_obj, **kwargs):
    try:
        obj_temp = model_obj()
        for key, value in kwargs.items():
            setattr(obj_temp, key, value)
        session.add(obj_temp)
        session.commit()
    except:
        session.rollback()


def get_all_models(model_obj):
    return session.query(model_obj).all()


def get_model_by_column_value(model_obj, column_value, value):
    return session.query(model_obj).filter(getattr(model_obj, column_value) == value).first()


def get_models_by_column_value(model_obj, column_value, value):
    return session.query(model_obj).filter(getattr(model_obj, column_value) == value).all()


def update_object_by_column(model_obj, column_value, value):
    setattr(model_obj, column_value, value)
    try:
        session.add(model_obj)
        session.commit()
    except:
        session.rollback()


def remove_object(model_obj):
    try:
        session.delete(model_obj)
        session.commit()
    except:
        session.rollback()


def get_object_columns(model_obj):
    return [column.key for column in model_obj.__table__.columns]
