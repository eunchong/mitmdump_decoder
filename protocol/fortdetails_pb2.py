# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fortdetails.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import holoholo_shared_pb2 as holoholo__shared__pb2

from holoholo_shared_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='fortdetails.proto',
  package='PGo',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x66ortdetails.proto\x12\x03PGo\x1a\x15holoholo_shared.proto\"\xd3\x02\n\x13\x46ortDetailsOutProto\x12\n\n\x02Id\x18\x01 \x01(\t\x12#\n\x04Team\x18\x02 \x01(\x0e\x32\x15.PGo.Custom_TeamColor\x12\"\n\x07Pokemon\x18\x03 \x01(\x0b\x32\x11.PGo.PokemonProto\x12\x0c\n\x04Name\x18\x04 \x01(\t\x12\x10\n\x08ImageUrl\x18\x05 \x03(\t\x12\n\n\x02\x46p\x18\x06 \x01(\x05\x12\x0f\n\x07Stamina\x18\x07 \x01(\x05\x12\x12\n\nMaxStamina\x18\x08 \x01(\x05\x12,\n\x08\x46ortType\x18\t \x01(\x0e\x32\x1a.PGo.Holoholo.Rpc.FortType\x12\x10\n\x08Latitude\x18\n \x01(\x01\x12\x11\n\tLongitude\x18\x0b \x01(\x01\x12\x13\n\x0b\x44\x65scription\x18\x0c \x01(\t\x12.\n\x08Modifier\x18\r \x03(\x0b\x32\x1c.PGo.ClientFortModifierProto\"\x82\x01\n\x17\x43lientFortModifierProto\x12,\n\x0cModifierType\x18\x01 \x01(\x0e\x32\x16.PGo.Holoholo.Rpc.Item\x12\x18\n\x10\x45xpirationTimeMs\x18\x02 \x01(\x03\x12\x1f\n\x17\x44\x65ployingPlayerCodename\x18\x03 \x01(\t\"C\n\x10\x46ortDetailsProto\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x10\n\x08Latitude\x18\x02 \x01(\x01\x12\x11\n\tLongitude\x18\x03 \x01(\x01\"\x81\x01\n\x0f\x46ortSearchProto\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x18\n\x10PlayerLatDegrees\x18\x02 \x01(\x01\x12\x18\n\x10PlayerLngDegrees\x18\x03 \x01(\x01\x12\x16\n\x0e\x46ortLatDegrees\x18\x04 \x01(\x01\x12\x16\n\x0e\x46ortLngDegrees\x18\x05 \x01(\x01\"I\n\x0e\x41wardItemProto\x12$\n\x04Item\x18\x01 \x01(\x0e\x32\x16.PGo.Holoholo.Rpc.Item\x12\x11\n\tItemCount\x18\x02 \x01(\x05\"\x85\x02\n\x12\x46ortSearchOutProto\x12\x41\n\x06Result\x18\x01 \x01(\x0e\x32\x31.PGo.Holoholo.Rpc.Types.FortSearchOutProto.Result\x12\"\n\x05Items\x18\x02 \x03(\x0b\x32\x13.PGo.AwardItemProto\x12\x13\n\x0bGemsAwarded\x18\x03 \x01(\x05\x12%\n\nEggPokemon\x18\x04 \x01(\x0b\x32\x11.PGo.PokemonProto\x12\x11\n\tXpAwarded\x18\x05 \x01(\x05\x12\x18\n\x10\x43ooldownComplete\x18\x06 \x01(\x03\x12\x1f\n\x17\x43hainHackSequenceNumber\x18\x07 \x01(\x05\"\x85\x01\n\x12GetGymDetailsProto\x12\r\n\x05GymId\x18\x01 \x01(\t\x12\x18\n\x10PlayerLatDegrees\x18\x02 \x01(\x01\x12\x18\n\x10PlayerLngDegrees\x18\x03 \x01(\x01\x12\x15\n\rGymLatDegrees\x18\x04 \x01(\x01\x12\x15\n\rGymLngDegrees\x18\x05 \x01(\x01\"\xe2\x01\n\x15GetGymDetailsOutProto\x12$\n\x08GymState\x18\x01 \x01(\x0b\x32\x12.PGo.GymStateProto\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x0b\n\x03Url\x18\x03 \x03(\t\x12\x35\n\x06Result\x18\x04 \x01(\x0e\x32%.PGo.GetGymDetailsOutProto.ResultEnum\x12\x13\n\x0b\x44\x65scription\x18\x05 \x01(\t\"<\n\nResultEnum\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x02\"k\n\rGymStateProto\x12*\n\x0b\x46ortMapData\x18\x01 \x01(\x0b\x32\x15.PGo.PokemonFortProto\x12.\n\rGymMembership\x18\x02 \x03(\x0b\x32\x17.PGo.GymMembershipProto\"u\n\x12GymMembershipProto\x12\"\n\x07Pokemon\x18\x01 \x01(\x0b\x32\x11.PGo.PokemonProto\x12;\n\x14TrainerPublicProfile\x18\x02 \x01(\x0b\x32\x1d.PGo.PlayerPublicProfileProto\"_\n\x18PlayerPublicProfileProto\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Level\x18\x02 \x01(\x05\x12&\n\x06\x41vatar\x18\x03 \x01(\x0b\x32\x16.PGo.PlayerAvatarProto\"\x99\x01\n\x11PlayerAvatarProto\x12\x0e\n\x06\x41vatar\x18\x08 \x01(\x05\x12\x0c\n\x04Skin\x18\x02 \x01(\x05\x12\x0c\n\x04Hair\x18\x03 \x01(\x05\x12\r\n\x05Shirt\x18\x04 \x01(\x05\x12\r\n\x05Pants\x18\x05 \x01(\x05\x12\x0b\n\x03Hat\x18\x06 \x01(\x05\x12\r\n\x05Shoes\x18\x07 \x01(\x05\x12\x0c\n\x04\x45yes\x18\t \x01(\x05\x12\x10\n\x08\x42\x61\x63kpack\x18\n \x01(\x05P\x00\x62\x06proto3')
  ,
  dependencies=[holoholo__shared__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETGYMDETAILSOUTPROTO_RESULTENUM = _descriptor.EnumDescriptor(
  name='ResultEnum',
  full_name='PGo.GetGymDetailsOutProto.ResultEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1367,
  serialized_end=1427,
)
_sym_db.RegisterEnumDescriptor(_GETGYMDETAILSOUTPROTO_RESULTENUM)


_FORTDETAILSOUTPROTO = _descriptor.Descriptor(
  name='FortDetailsOutProto',
  full_name='PGo.FortDetailsOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='PGo.FortDetailsOutProto.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Team', full_name='PGo.FortDetailsOutProto.Team', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PGo.FortDetailsOutProto.Pokemon', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='PGo.FortDetailsOutProto.Name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ImageUrl', full_name='PGo.FortDetailsOutProto.ImageUrl', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fp', full_name='PGo.FortDetailsOutProto.Fp', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Stamina', full_name='PGo.FortDetailsOutProto.Stamina', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MaxStamina', full_name='PGo.FortDetailsOutProto.MaxStamina', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FortType', full_name='PGo.FortDetailsOutProto.FortType', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='PGo.FortDetailsOutProto.Latitude', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='PGo.FortDetailsOutProto.Longitude', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Description', full_name='PGo.FortDetailsOutProto.Description', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Modifier', full_name='PGo.FortDetailsOutProto.Modifier', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=389,
)


_CLIENTFORTMODIFIERPROTO = _descriptor.Descriptor(
  name='ClientFortModifierProto',
  full_name='PGo.ClientFortModifierProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ModifierType', full_name='PGo.ClientFortModifierProto.ModifierType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ExpirationTimeMs', full_name='PGo.ClientFortModifierProto.ExpirationTimeMs', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DeployingPlayerCodename', full_name='PGo.ClientFortModifierProto.DeployingPlayerCodename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=522,
)


_FORTDETAILSPROTO = _descriptor.Descriptor(
  name='FortDetailsProto',
  full_name='PGo.FortDetailsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='PGo.FortDetailsProto.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Latitude', full_name='PGo.FortDetailsProto.Latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Longitude', full_name='PGo.FortDetailsProto.Longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=591,
)


_FORTSEARCHPROTO = _descriptor.Descriptor(
  name='FortSearchProto',
  full_name='PGo.FortSearchProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='PGo.FortSearchProto.Id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PlayerLatDegrees', full_name='PGo.FortSearchProto.PlayerLatDegrees', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PlayerLngDegrees', full_name='PGo.FortSearchProto.PlayerLngDegrees', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FortLatDegrees', full_name='PGo.FortSearchProto.FortLatDegrees', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FortLngDegrees', full_name='PGo.FortSearchProto.FortLngDegrees', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=594,
  serialized_end=723,
)


_AWARDITEMPROTO = _descriptor.Descriptor(
  name='AwardItemProto',
  full_name='PGo.AwardItemProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Item', full_name='PGo.AwardItemProto.Item', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ItemCount', full_name='PGo.AwardItemProto.ItemCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=798,
)


_FORTSEARCHOUTPROTO = _descriptor.Descriptor(
  name='FortSearchOutProto',
  full_name='PGo.FortSearchOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='PGo.FortSearchOutProto.Result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Items', full_name='PGo.FortSearchOutProto.Items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GemsAwarded', full_name='PGo.FortSearchOutProto.GemsAwarded', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EggPokemon', full_name='PGo.FortSearchOutProto.EggPokemon', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='XpAwarded', full_name='PGo.FortSearchOutProto.XpAwarded', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='CooldownComplete', full_name='PGo.FortSearchOutProto.CooldownComplete', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ChainHackSequenceNumber', full_name='PGo.FortSearchOutProto.ChainHackSequenceNumber', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=1062,
)


_GETGYMDETAILSPROTO = _descriptor.Descriptor(
  name='GetGymDetailsProto',
  full_name='PGo.GetGymDetailsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='GymId', full_name='PGo.GetGymDetailsProto.GymId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PlayerLatDegrees', full_name='PGo.GetGymDetailsProto.PlayerLatDegrees', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PlayerLngDegrees', full_name='PGo.GetGymDetailsProto.PlayerLngDegrees', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GymLatDegrees', full_name='PGo.GetGymDetailsProto.GymLatDegrees', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GymLngDegrees', full_name='PGo.GetGymDetailsProto.GymLngDegrees', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1065,
  serialized_end=1198,
)


_GETGYMDETAILSOUTPROTO = _descriptor.Descriptor(
  name='GetGymDetailsOutProto',
  full_name='PGo.GetGymDetailsOutProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='GymState', full_name='PGo.GetGymDetailsOutProto.GymState', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='PGo.GetGymDetailsOutProto.Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Url', full_name='PGo.GetGymDetailsOutProto.Url', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Result', full_name='PGo.GetGymDetailsOutProto.Result', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Description', full_name='PGo.GetGymDetailsOutProto.Description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETGYMDETAILSOUTPROTO_RESULTENUM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1201,
  serialized_end=1427,
)


_GYMSTATEPROTO = _descriptor.Descriptor(
  name='GymStateProto',
  full_name='PGo.GymStateProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FortMapData', full_name='PGo.GymStateProto.FortMapData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GymMembership', full_name='PGo.GymStateProto.GymMembership', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1429,
  serialized_end=1536,
)


_GYMMEMBERSHIPPROTO = _descriptor.Descriptor(
  name='GymMembershipProto',
  full_name='PGo.GymMembershipProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PGo.GymMembershipProto.Pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TrainerPublicProfile', full_name='PGo.GymMembershipProto.TrainerPublicProfile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1538,
  serialized_end=1655,
)


_PLAYERPUBLICPROFILEPROTO = _descriptor.Descriptor(
  name='PlayerPublicProfileProto',
  full_name='PGo.PlayerPublicProfileProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='PGo.PlayerPublicProfileProto.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Level', full_name='PGo.PlayerPublicProfileProto.Level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Avatar', full_name='PGo.PlayerPublicProfileProto.Avatar', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1657,
  serialized_end=1752,
)


_PLAYERAVATARPROTO = _descriptor.Descriptor(
  name='PlayerAvatarProto',
  full_name='PGo.PlayerAvatarProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Avatar', full_name='PGo.PlayerAvatarProto.Avatar', index=0,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Skin', full_name='PGo.PlayerAvatarProto.Skin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hair', full_name='PGo.PlayerAvatarProto.Hair', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Shirt', full_name='PGo.PlayerAvatarProto.Shirt', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pants', full_name='PGo.PlayerAvatarProto.Pants', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hat', full_name='PGo.PlayerAvatarProto.Hat', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Shoes', full_name='PGo.PlayerAvatarProto.Shoes', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Eyes', full_name='PGo.PlayerAvatarProto.Eyes', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Backpack', full_name='PGo.PlayerAvatarProto.Backpack', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1755,
  serialized_end=1908,
)

_FORTDETAILSOUTPROTO.fields_by_name['Team'].enum_type = holoholo__shared__pb2._CUSTOM_TEAMCOLOR
_FORTDETAILSOUTPROTO.fields_by_name['Pokemon'].message_type = holoholo__shared__pb2._POKEMONPROTO
_FORTDETAILSOUTPROTO.fields_by_name['FortType'].enum_type = holoholo__shared__pb2._HOLOHOLO_RPC_FORTTYPE
_FORTDETAILSOUTPROTO.fields_by_name['Modifier'].message_type = _CLIENTFORTMODIFIERPROTO
_CLIENTFORTMODIFIERPROTO.fields_by_name['ModifierType'].enum_type = holoholo__shared__pb2._HOLOHOLO_RPC_ITEM
_AWARDITEMPROTO.fields_by_name['Item'].enum_type = holoholo__shared__pb2._HOLOHOLO_RPC_ITEM
_FORTSEARCHOUTPROTO.fields_by_name['Result'].enum_type = holoholo__shared__pb2._HOLOHOLO_RPC_TYPES_FORTSEARCHOUTPROTO_RESULT
_FORTSEARCHOUTPROTO.fields_by_name['Items'].message_type = _AWARDITEMPROTO
_FORTSEARCHOUTPROTO.fields_by_name['EggPokemon'].message_type = holoholo__shared__pb2._POKEMONPROTO
_GETGYMDETAILSOUTPROTO.fields_by_name['GymState'].message_type = _GYMSTATEPROTO
_GETGYMDETAILSOUTPROTO.fields_by_name['Result'].enum_type = _GETGYMDETAILSOUTPROTO_RESULTENUM
_GETGYMDETAILSOUTPROTO_RESULTENUM.containing_type = _GETGYMDETAILSOUTPROTO
_GYMSTATEPROTO.fields_by_name['FortMapData'].message_type = holoholo__shared__pb2._POKEMONFORTPROTO
_GYMSTATEPROTO.fields_by_name['GymMembership'].message_type = _GYMMEMBERSHIPPROTO
_GYMMEMBERSHIPPROTO.fields_by_name['Pokemon'].message_type = holoholo__shared__pb2._POKEMONPROTO
_GYMMEMBERSHIPPROTO.fields_by_name['TrainerPublicProfile'].message_type = _PLAYERPUBLICPROFILEPROTO
_PLAYERPUBLICPROFILEPROTO.fields_by_name['Avatar'].message_type = _PLAYERAVATARPROTO
DESCRIPTOR.message_types_by_name['FortDetailsOutProto'] = _FORTDETAILSOUTPROTO
DESCRIPTOR.message_types_by_name['ClientFortModifierProto'] = _CLIENTFORTMODIFIERPROTO
DESCRIPTOR.message_types_by_name['FortDetailsProto'] = _FORTDETAILSPROTO
DESCRIPTOR.message_types_by_name['FortSearchProto'] = _FORTSEARCHPROTO
DESCRIPTOR.message_types_by_name['AwardItemProto'] = _AWARDITEMPROTO
DESCRIPTOR.message_types_by_name['FortSearchOutProto'] = _FORTSEARCHOUTPROTO
DESCRIPTOR.message_types_by_name['GetGymDetailsProto'] = _GETGYMDETAILSPROTO
DESCRIPTOR.message_types_by_name['GetGymDetailsOutProto'] = _GETGYMDETAILSOUTPROTO
DESCRIPTOR.message_types_by_name['GymStateProto'] = _GYMSTATEPROTO
DESCRIPTOR.message_types_by_name['GymMembershipProto'] = _GYMMEMBERSHIPPROTO
DESCRIPTOR.message_types_by_name['PlayerPublicProfileProto'] = _PLAYERPUBLICPROFILEPROTO
DESCRIPTOR.message_types_by_name['PlayerAvatarProto'] = _PLAYERAVATARPROTO

FortDetailsOutProto = _reflection.GeneratedProtocolMessageType('FortDetailsOutProto', (_message.Message,), dict(
  DESCRIPTOR = _FORTDETAILSOUTPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortDetailsOutProto)
  ))
_sym_db.RegisterMessage(FortDetailsOutProto)

ClientFortModifierProto = _reflection.GeneratedProtocolMessageType('ClientFortModifierProto', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTFORTMODIFIERPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.ClientFortModifierProto)
  ))
_sym_db.RegisterMessage(ClientFortModifierProto)

FortDetailsProto = _reflection.GeneratedProtocolMessageType('FortDetailsProto', (_message.Message,), dict(
  DESCRIPTOR = _FORTDETAILSPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortDetailsProto)
  ))
_sym_db.RegisterMessage(FortDetailsProto)

FortSearchProto = _reflection.GeneratedProtocolMessageType('FortSearchProto', (_message.Message,), dict(
  DESCRIPTOR = _FORTSEARCHPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortSearchProto)
  ))
_sym_db.RegisterMessage(FortSearchProto)

AwardItemProto = _reflection.GeneratedProtocolMessageType('AwardItemProto', (_message.Message,), dict(
  DESCRIPTOR = _AWARDITEMPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.AwardItemProto)
  ))
_sym_db.RegisterMessage(AwardItemProto)

FortSearchOutProto = _reflection.GeneratedProtocolMessageType('FortSearchOutProto', (_message.Message,), dict(
  DESCRIPTOR = _FORTSEARCHOUTPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.FortSearchOutProto)
  ))
_sym_db.RegisterMessage(FortSearchOutProto)

GetGymDetailsProto = _reflection.GeneratedProtocolMessageType('GetGymDetailsProto', (_message.Message,), dict(
  DESCRIPTOR = _GETGYMDETAILSPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GetGymDetailsProto)
  ))
_sym_db.RegisterMessage(GetGymDetailsProto)

GetGymDetailsOutProto = _reflection.GeneratedProtocolMessageType('GetGymDetailsOutProto', (_message.Message,), dict(
  DESCRIPTOR = _GETGYMDETAILSOUTPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GetGymDetailsOutProto)
  ))
_sym_db.RegisterMessage(GetGymDetailsOutProto)

GymStateProto = _reflection.GeneratedProtocolMessageType('GymStateProto', (_message.Message,), dict(
  DESCRIPTOR = _GYMSTATEPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GymStateProto)
  ))
_sym_db.RegisterMessage(GymStateProto)

GymMembershipProto = _reflection.GeneratedProtocolMessageType('GymMembershipProto', (_message.Message,), dict(
  DESCRIPTOR = _GYMMEMBERSHIPPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.GymMembershipProto)
  ))
_sym_db.RegisterMessage(GymMembershipProto)

PlayerPublicProfileProto = _reflection.GeneratedProtocolMessageType('PlayerPublicProfileProto', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERPUBLICPROFILEPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.PlayerPublicProfileProto)
  ))
_sym_db.RegisterMessage(PlayerPublicProfileProto)

PlayerAvatarProto = _reflection.GeneratedProtocolMessageType('PlayerAvatarProto', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERAVATARPROTO,
  __module__ = 'fortdetails_pb2'
  # @@protoc_insertion_point(class_scope:PGo.PlayerAvatarProto)
  ))
_sym_db.RegisterMessage(PlayerAvatarProto)


# @@protoc_insertion_point(module_scope)
