# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from . import path

# query params


class EnumQueryStringArraySchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    ">": "GREATER_THAN",
                    "$": "DOLLAR",
                }
            
            @schemas.classproperty
            def GREATER_THAN(cls):
                return cls(">")
            
            @schemas.classproperty
            def DOLLAR(cls):
                return cls("$")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EnumQueryStringArraySchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class EnumQueryStringSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "_abc": "_ABC",
            "-efg": "EFG",
            "(xyz)": "XYZ",
        }
    
    @schemas.classproperty
    def _ABC(cls):
        return cls("_abc")
    
    @schemas.classproperty
    def EFG(cls):
        return cls("-efg")
    
    @schemas.classproperty
    def XYZ(cls):
        return cls("(xyz)")


class EnumQueryIntegerSchema(
    schemas.EnumBase,
    schemas.Int32Schema
):


    class MetaOapg:
        format = 'int32'
        enum_value_to_name = {
            1: "POSITIVE_1",
            -2: "NEGATIVE_2",
        }
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1)
    
    @schemas.classproperty
    def NEGATIVE_2(cls):
        return cls(-2)


class EnumQueryDoubleSchema(
    schemas.EnumBase,
    schemas.Float64Schema
):


    class MetaOapg:
        format = 'double'
        enum_value_to_name = {
            1.1: "POSITIVE_1_PT_1",
            -1.2: "NEGATIVE_1_PT_2",
        }
    
    @schemas.classproperty
    def POSITIVE_1_PT_1(cls):
        return cls(1.1)
    
    @schemas.classproperty
    def NEGATIVE_1_PT_2(cls):
        return cls(-1.2)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'enum_query_string_array': typing.Union[EnumQueryStringArraySchema, list, tuple, ],
        'enum_query_string': typing.Union[EnumQueryStringSchema, str, ],
        'enum_query_integer': typing.Union[EnumQueryIntegerSchema, decimal.Decimal, int, ],
        'enum_query_double': typing.Union[EnumQueryDoubleSchema, decimal.Decimal, int, float, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_enum_query_string_array = api_client.QueryParameter(
    name="enum_query_string_array",
    style=api_client.ParameterStyle.FORM,
    schema=EnumQueryStringArraySchema,
    explode=True,
)
request_query_enum_query_string = api_client.QueryParameter(
    name="enum_query_string",
    style=api_client.ParameterStyle.FORM,
    schema=EnumQueryStringSchema,
    explode=True,
)
request_query_enum_query_integer = api_client.QueryParameter(
    name="enum_query_integer",
    style=api_client.ParameterStyle.FORM,
    schema=EnumQueryIntegerSchema,
    explode=True,
)
request_query_enum_query_double = api_client.QueryParameter(
    name="enum_query_double",
    style=api_client.ParameterStyle.FORM,
    schema=EnumQueryDoubleSchema,
    explode=True,
)
# header params


class EnumHeaderStringArraySchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    ">": "GREATER_THAN",
                    "$": "DOLLAR",
                }
            
            @schemas.classproperty
            def GREATER_THAN(cls):
                return cls(">")
            
            @schemas.classproperty
            def DOLLAR(cls):
                return cls("$")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EnumHeaderStringArraySchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class EnumHeaderStringSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "_abc": "_ABC",
            "-efg": "EFG",
            "(xyz)": "XYZ",
        }
    
    @schemas.classproperty
    def _ABC(cls):
        return cls("_abc")
    
    @schemas.classproperty
    def EFG(cls):
        return cls("-efg")
    
    @schemas.classproperty
    def XYZ(cls):
        return cls("(xyz)")
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'enum_header_string_array': typing.Union[EnumHeaderStringArraySchema, list, tuple, ],
        'enum_header_string': typing.Union[EnumHeaderStringSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_enum_header_string_array = api_client.HeaderParameter(
    name="enum_header_string_array",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EnumHeaderStringArraySchema,
)
request_header_enum_header_string = api_client.HeaderParameter(
    name="enum_header_string",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EnumHeaderStringSchema,
)
# body param


class SchemaForRequestBodyApplicationXWwwFormUrlencoded(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class enum_form_string_array(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                ">": "GREATER_THAN",
                                "$": "DOLLAR",
                            }
                        
                        @schemas.classproperty
                        def GREATER_THAN(cls):
                            return cls(">")
                        
                        @schemas.classproperty
                        def DOLLAR(cls):
                            return cls("$")
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'enum_form_string_array':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class enum_form_string(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "_abc": "_ABC",
                        "-efg": "EFG",
                        "(xyz)": "XYZ",
                    }
                
                @schemas.classproperty
                def _ABC(cls):
                    return cls("_abc")
                
                @schemas.classproperty
                def EFG(cls):
                    return cls("-efg")
                
                @schemas.classproperty
                def XYZ(cls):
                    return cls("(xyz)")
            __annotations__ = {
                "enum_form_string_array": enum_form_string_array,
                "enum_form_string": enum_form_string,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_form_string_array"]) -> MetaOapg.properties.enum_form_string_array: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_form_string"]) -> MetaOapg.properties.enum_form_string: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enum_form_string_array", "enum_form_string", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enum_form_string_array"]) -> typing.Union[MetaOapg.properties.enum_form_string_array, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enum_form_string"]) -> typing.Union[MetaOapg.properties.enum_form_string, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enum_form_string_array", "enum_form_string", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        enum_form_string_array: typing.Union[MetaOapg.properties.enum_form_string_array, list, tuple, schemas.Unset] = schemas.unset,
        enum_form_string: typing.Union[MetaOapg.properties.enum_form_string, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationXWwwFormUrlencoded':
        return super().__new__(
            cls,
            *args,
            enum_form_string_array=enum_form_string_array,
            enum_form_string=enum_form_string,
            _configuration=_configuration,
            **kwargs,
        )


request_body_body = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)
_status_code_to_response = {
    '400': _response_for_400,
    '404': _response_for_404,
}


class BaseApi(api_client.Api):

    @typing.overload
    def _enum_parameters_oapg(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        api_client.ApiResponse,
        api_client.ApiResponse,
    ]:
        ...

    @typing.overload
    def _enum_parameters_oapg(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    def _enum_parameters_oapg(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponse,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        To test enum parameters
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_enum_query_string_array,
            request_query_enum_query_string,
            request_query_enum_query_integer,
            request_query_enum_query_double,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_enum_header_string_array,
            request_header_enum_header_string,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class EnumParameters(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def enum_parameters(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        api_client.ApiResponse,
        api_client.ApiResponse,
    ]:
        ...

    @typing.overload
    def enum_parameters(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    def enum_parameters(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponse,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._enum_parameters_oapg(
            body=body,
            query_params=query_params,
            header_params=header_params,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        api_client.ApiResponse,
        api_client.ApiResponse,
    ]:
        ...

    @typing.overload
    def get(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    def get(
        self: BaseApi,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        api_client.ApiResponse,
        api_client.ApiResponse,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._enum_parameters_oapg(
            body=body,
            query_params=query_params,
            header_params=header_params,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


