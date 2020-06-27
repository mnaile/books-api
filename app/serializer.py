from app.model import Books
from marshmallow import fields, validate
from extensions.extensions import ma


class BookSchema(ma.SQLAlchemyAutoSchema):

    user_id = fields.Integer()
    title = fields.String(required=True, validate=[validate.Length(min=2, max=40)])
    page = fields.Integer(required=True)
    author = fields.String(required=True, validate=[validate.Length(min=2, max=100)])

    class Meta:
        model = Books
        load_instance = True

class UpdateBookSchema(ma.SQLAlchemyAutoSchema):

    user_id = fields.Integer()
    title = fields.String(validate=[validate.Length(min=2, max=40)])
    page = fields.Integer()
    author = fields.String(validate=[validate.Length(min=2, max=100)])

