# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Bar: typing_extensions.TypeAlias = schemas.StrSchema
Foo: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "bar": typing.Type[Bar],
        "foo": typing.Type[Foo],
    }
)


class HasOnlyReadOnlyDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "bar",
        "foo",
    })
    
    def __new__(
        cls,
        *,
        bar: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        foo: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("bar", bar),
            ("foo", foo),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(HasOnlyReadOnlyDictInput, arg_)
        return HasOnlyReadOnly.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            HasOnlyReadOnlyDictInput,
            HasOnlyReadOnlyDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HasOnlyReadOnlyDict:
        return HasOnlyReadOnly.validate(arg, configuration=configuration)
    
    @property
    def bar(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("bar", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def foo(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("foo", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
HasOnlyReadOnlyDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class HasOnlyReadOnly(
    schemas.Schema[HasOnlyReadOnlyDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: HasOnlyReadOnlyDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            HasOnlyReadOnlyDictInput,
            HasOnlyReadOnlyDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HasOnlyReadOnlyDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

