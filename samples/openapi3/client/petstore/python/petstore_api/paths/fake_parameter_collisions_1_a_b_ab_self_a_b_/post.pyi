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

# query params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
AbSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
# header params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
# path params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
AbSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
# cookie params
Model1Schema = schemas.StrSchema
ABSchema = schemas.StrSchema
AbSchema = schemas.StrSchema
ModelSelfSchema = schemas.StrSchema
ABSchema = schemas.StrSchema
# body param
SchemaForRequestBodyApplicationJson = schemas.AnyTypeSchema
SchemaFor200ResponseBodyApplicationJson = schemas.AnyTypeSchema
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    @typing.overload
    def _parameter_collisions_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        ApiResponseFor200,
    ]:
        ...

    @typing.overload
    def _parameter_collisions_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def _parameter_collisions_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def _parameter_collisions_oapg(
        self,
        body,
        query_params = frozendict.frozendict(),
        header_params = frozendict.frozendict(),
        path_params = frozendict.frozendict(),
        cookie_params = frozendict.frozendict(),
        content_type = 'application/json',
        accept_content_types = _all_accept_content_types,
        stream = False,
        timeout = None,
        skip_deserialization = False,
    ):
        """
        parameter collision case
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        self._verify_typed_dict_inputs_oapg(RequestCookieParams, cookie_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path__3,
            request_path_a_b5,
            request_path_ab2,
            request_path__self3,
            request_path_a_b6,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query__1,
            request_query_a_b,
            request_query_ab,
            request_query__self,
            request_query_a_b2,
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
            request_header__2,
            request_header_a_b3,
            request_header__self2,
            request_header_a_b4,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

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
            method='post'.upper(),
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


class ParameterCollisions(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def parameter_collisions(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        ApiResponseFor200,
    ]:
        ...

    @typing.overload
    def parameter_collisions(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def parameter_collisions(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def parameter_collisions(
        self,
        body,
        query_params = frozendict.frozendict(),
        header_params = frozendict.frozendict(),
        path_params = frozendict.frozendict(),
        cookie_params = frozendict.frozendict(),
        content_type = 'application/json',
        accept_content_types = _all_accept_content_types,
        stream = False,
        timeout = None,
        skip_deserialization = False,
    ):
        return self._parameter_collisions_oapg(
            body=body,
            query_params=query_params,
            header_params=header_params,
            path_params=path_params,
            cookie_params=cookie_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False,
    ) -> typing.Union[
        ApiResponseFor200,
    ]:
        ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = True,
    ) -> api_client.ApiResponseWithoutDeserialization:
        ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParams = frozendict.frozendict(),
        header_params: RequestHeaderParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        cookie_params: RequestCookieParams = frozendict.frozendict(),
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        ...

    def post(
        self,
        body,
        query_params = frozendict.frozendict(),
        header_params = frozendict.frozendict(),
        path_params = frozendict.frozendict(),
        cookie_params = frozendict.frozendict(),
        content_type = 'application/json',
        accept_content_types = _all_accept_content_types,
        stream = False,
        timeout = None,
        skip_deserialization = False,
    ):
        return self._parameter_collisions_oapg(
            body=body,
            query_params=query_params,
            header_params=header_params,
            path_params=path_params,
            cookie_params=cookie_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


