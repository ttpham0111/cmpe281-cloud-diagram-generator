from app.db.tables import Field


def get_fields(user, session):
    return session.query(Field).filter_by(user_id=user.id).all()


def create_or_update_field(user, new_field, session):
    field = session.query(Field).filter_by(user_id=user.id, name=new_field['name']).one_or_none()
    if field:
        field.type = new_field['type']
        field.value = new_field['value']
    else:
        field = Field(
            user_id=user.id,
            name=new_field['name'],
            type=new_field['type'],
            value=new_field['value']
        )
        session.add(field)

    session.commit()
    session.refresh(field)

    return field


def delete_field(user, field_name, session):
    field = session.query(Field).filter_by(user_id=user.id, name=field_name).one()
    session.delete(field)
    session.commit()
