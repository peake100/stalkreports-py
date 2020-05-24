# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stalk_proto/reporter.proto

from protogen.stalk_proto import models_pb2 as stalk__proto_dot_models__pb2
from protogen.stalk_proto.google.api import (
    annotations_pb2 as stalk__proto_dot_google_dot_api_dot_annotations__pb2,
)
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="stalk_proto/reporter.proto",
    package="proto",
    syntax="proto3",
    serialized_options=b"Z1github.com/peake100/stalkforecaster-go/stalkproto",
    serialized_pb=b'\n\x1astalk_proto/reporter.proto\x12\x05proto\x1a(stalk_proto/google/api/annotations.proto\x1a\x18stalk_proto/models.proto2l\n\rStalkReporter\x12[\n\rForecastChart\x12\x17.proto.ReqForecastChart\x1a\x10.proto.RespChart"\x1f\x82\xd3\xe4\x93\x02\x19"\x14/api/charts/forecast:\x01*B3Z1github.com/peake100/stalkforecaster-go/stalkprotob\x06proto3',
    dependencies=[
        stalk__proto_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        stalk__proto_dot_models__pb2.DESCRIPTOR,
    ],
)


_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_STALKREPORTER = _descriptor.ServiceDescriptor(
    name="StalkReporter",
    full_name="proto.StalkReporter",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=105,
    serialized_end=213,
    methods=[
        _descriptor.MethodDescriptor(
            name="ForecastChart",
            full_name="proto.StalkReporter.ForecastChart",
            index=0,
            containing_service=None,
            input_type=stalk__proto_dot_models__pb2._REQFORECASTCHART,
            output_type=stalk__proto_dot_models__pb2._RESPCHART,
            serialized_options=b'\202\323\344\223\002\031"\024/api/charts/forecast:\001*',
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_STALKREPORTER)

DESCRIPTOR.services_by_name["StalkReporter"] = _STALKREPORTER

# @@protoc_insertion_point(module_scope)
