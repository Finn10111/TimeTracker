from marshmallow import SchemaOpts
from marshmallow import pre_load, post_dump
from marshmallow_sqlalchemy import ModelSchemaOpts, ModelConverter, ModelSchema
from .. import ma
from .. import db


class NamespaceOpts(ModelSchemaOpts):
    """Same as the default class Meta options, but adds "name" and
    "plural_name" options for enveloping.
    """

    def __init__(self, meta, **kwargs):
        SchemaOpts.__init__(self, meta, **kwargs)
        self.name = getattr(meta, "name", None)
        self.plural_name = getattr(meta, "plural_name", self.name)
        self.model = getattr(meta, "model", None)
        self.model_converter = getattr(meta, "model_converter", ModelConverter)
        self.include_fk = getattr(meta, "include_fk", False)
        self.transient = getattr(meta, "transient", False)
        self.sqla_session = db.session
        self.load_instance = True
        self.include_relationships = True


#class NamespacedSchema(ma.SQLAlchemySchema):
class NamespacedSchema(ModelSchema):
    OPTIONS_CLASS = NamespaceOpts

    @pre_load(pass_many=True)
    def unwrap_envelope(self, data, many, **kwargs):
        key = self.opts.plural_name if many else self.opts.name
        if key in data:
            return data[key]
        else:
            return data

    @post_dump(pass_many=True)
    def wrap_with_envelope(self, data, many, **kwargs):
        if 'noenvelope' in self.context and self.context['noenvelope']:
            return data
        else:
            key = self.opts.plural_name if many else self.opts.name
            return {key: data}
