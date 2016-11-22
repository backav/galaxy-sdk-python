# encoding: utf-8
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import sds.errors.ttypes
import sds.common.ttypes
import sds.auth.ttypes
import sds.table.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class ClientMetricType(object):
  """
  客户端metrics的类型
  """
  Letency = 1

  _VALUES_TO_NAMES = {
    1: "Letency",
  }

  _NAMES_TO_VALUES = {
    "Letency": 1,
  }

class LatencyMetricType(object):
  """
  客户端metrics请求延迟的类型
  """
  ExecutionTime = 1

  _VALUES_TO_NAMES = {
    1: "ExecutionTime",
  }

  _NAMES_TO_VALUES = {
    "ExecutionTime": 1,
  }

class MetricKey(object):
  """
  系统统计指标类型
  """
  METER_METRIC_MIN = 0
  READ_ALLOWED = 1
  READ_THROTTLED = 2
  WRITE_ALLOWED = 3
  WRITE_THROTTLED = 4
  ACTION_SUCCESS = 5
  ACTION_CLIENT_ERROR = 6
  ACTION_SYSTEM_ERROR = 7
  METER_METRIC_MAX = 49
  HISTOGRAM_METRIC_MIN = 50
  CREATE_LATENCY = 51
  DROP_LATENCY = 52
  DESCRIBE_LATENCY = 53
  ALTER_LATENCY = 54
  ENABLE_LATENCY = 55
  DISABLE_LATENCY = 56
  METRICQUERY_LATENCY = 57
  GET_LATENCY = 58
  PUT_LATENCY = 59
  INCREMENT_LATENCY = 60
  DELETE_LATENCY = 61
  SCAN_LATENCY = 62
  BATCH_LATENCY = 63
  HISTOGRAM_METRIC_MAX = 100

  _VALUES_TO_NAMES = {
    0: "METER_METRIC_MIN",
    1: "READ_ALLOWED",
    2: "READ_THROTTLED",
    3: "WRITE_ALLOWED",
    4: "WRITE_THROTTLED",
    5: "ACTION_SUCCESS",
    6: "ACTION_CLIENT_ERROR",
    7: "ACTION_SYSTEM_ERROR",
    49: "METER_METRIC_MAX",
    50: "HISTOGRAM_METRIC_MIN",
    51: "CREATE_LATENCY",
    52: "DROP_LATENCY",
    53: "DESCRIBE_LATENCY",
    54: "ALTER_LATENCY",
    55: "ENABLE_LATENCY",
    56: "DISABLE_LATENCY",
    57: "METRICQUERY_LATENCY",
    58: "GET_LATENCY",
    59: "PUT_LATENCY",
    60: "INCREMENT_LATENCY",
    61: "DELETE_LATENCY",
    62: "SCAN_LATENCY",
    63: "BATCH_LATENCY",
    100: "HISTOGRAM_METRIC_MAX",
  }

  _NAMES_TO_VALUES = {
    "METER_METRIC_MIN": 0,
    "READ_ALLOWED": 1,
    "READ_THROTTLED": 2,
    "WRITE_ALLOWED": 3,
    "WRITE_THROTTLED": 4,
    "ACTION_SUCCESS": 5,
    "ACTION_CLIENT_ERROR": 6,
    "ACTION_SYSTEM_ERROR": 7,
    "METER_METRIC_MAX": 49,
    "HISTOGRAM_METRIC_MIN": 50,
    "CREATE_LATENCY": 51,
    "DROP_LATENCY": 52,
    "DESCRIBE_LATENCY": 53,
    "ALTER_LATENCY": 54,
    "ENABLE_LATENCY": 55,
    "DISABLE_LATENCY": 56,
    "METRICQUERY_LATENCY": 57,
    "GET_LATENCY": 58,
    "PUT_LATENCY": 59,
    "INCREMENT_LATENCY": 60,
    "DELETE_LATENCY": 61,
    "SCAN_LATENCY": 62,
    "BATCH_LATENCY": 63,
    "HISTOGRAM_METRIC_MAX": 100,
  }

class MetricType(object):
  """
  统计指标的子类型
  (MetricKey, MetricType) 元组唯一确定一个统计指标
  """
  COUNT = 1
  M1_RATE = 2
  M5_RATE = 3
  M15_RATE = 4
  MEAN = 5
  STDDEV = 6
  P50 = 7
  P75 = 8
  P95 = 9
  P98 = 10
  P99 = 11

  _VALUES_TO_NAMES = {
    1: "COUNT",
    2: "M1_RATE",
    3: "M5_RATE",
    4: "M15_RATE",
    5: "MEAN",
    6: "STDDEV",
    7: "P50",
    8: "P75",
    9: "P95",
    10: "P98",
    11: "P99",
  }

  _NAMES_TO_VALUES = {
    "COUNT": 1,
    "M1_RATE": 2,
    "M5_RATE": 3,
    "M15_RATE": 4,
    "MEAN": 5,
    "STDDEV": 6,
    "P50": 7,
    "P75": 8,
    "P95": 9,
    "P98": 10,
    "P99": 11,
  }

class TimeSpanUnit(object):
  """
  时间间隔单位，用于查询统计指标时的下采样
  """
  SECONDS = 1
  MINUTES = 2
  HOURS = 3

  _VALUES_TO_NAMES = {
    1: "SECONDS",
    2: "MINUTES",
    3: "HOURS",
  }

  _NAMES_TO_VALUES = {
    "SECONDS": 1,
    "MINUTES": 2,
    "HOURS": 3,
  }


class AppInfo(object):
  """
  应用信息

  Attributes:
   - appId: 小米应用ID
   - developerId: 小米开发者ID (注意：不同于小米ID)
   - tableMappings: 表到表ID的映射
   - oauthAppMapping: 应用OAuth信息, OAuth提供方到第三方OAuth应用信息(如OAuth AppID)的映射
   - appName: 小米应用名称
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'appId', None, None, ), # 1
    (2, TType.STRING, 'developerId', None, None, ), # 2
    (3, TType.MAP, 'tableMappings', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.MAP, 'oauthAppMapping', (TType.STRING,None,TType.STRING,None), None, ), # 4
    (5, TType.STRING, 'appName', None, None, ), # 5
  )

  def __init__(self, appId=None, developerId=None, tableMappings=None, oauthAppMapping=None, appName=None,):
    self.appId = appId
    self.developerId = developerId
    self.tableMappings = tableMappings
    self.oauthAppMapping = oauthAppMapping
    self.appName = appName

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.appId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.developerId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.tableMappings = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in range(_size0):
            _key5 = iprot.readString();
            _val6 = iprot.readString();
            self.tableMappings[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.oauthAppMapping = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin()
          for _i11 in range(_size7):
            _key12 = iprot.readString();
            _val13 = iprot.readString();
            self.oauthAppMapping[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.appName = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AppInfo')
    if self.appId is not None:
      oprot.writeFieldBegin('appId', TType.STRING, 1)
      oprot.writeString(self.appId)
      oprot.writeFieldEnd()
    if self.developerId is not None:
      oprot.writeFieldBegin('developerId', TType.STRING, 2)
      oprot.writeString(self.developerId)
      oprot.writeFieldEnd()
    if self.tableMappings is not None:
      oprot.writeFieldBegin('tableMappings', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.tableMappings))
      for kiter14,viter15 in list(self.tableMappings.items()):
        oprot.writeString(kiter14)
        oprot.writeString(viter15)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.oauthAppMapping is not None:
      oprot.writeFieldBegin('oauthAppMapping', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.oauthAppMapping))
      for kiter16,viter17 in list(self.oauthAppMapping.items()):
        oprot.writeString(kiter16)
        oprot.writeString(viter17)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.appName is not None:
      oprot.writeFieldBegin('appName', TType.STRING, 5)
      oprot.writeString(self.appName)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.appId)
    value = (value * 31) ^ hash(self.developerId)
    value = (value * 31) ^ hash(self.tableMappings)
    value = (value * 31) ^ hash(self.oauthAppMapping)
    value = (value * 31) ^ hash(self.appName)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MetricData(object):
  """
  客户端metrics数据结构

  Attributes:
   - clientMetricType: 设置/获取metrics的类型
   - metricName: 客户端请求调用的接口名称.实际计算的数据类型
  e.g. createTable.ExecutionTime
   - value: 实际计算的数值
   - timeStamp: 客户端请求返回的时间戳
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'clientMetricType', None, None, ), # 1
    (2, TType.STRING, 'metricName', None, None, ), # 2
    (3, TType.I64, 'value', None, None, ), # 3
    (4, TType.I64, 'timeStamp', None, None, ), # 4
  )

  def __init__(self, clientMetricType=None, metricName=None, value=None, timeStamp=None,):
    self.clientMetricType = clientMetricType
    self.metricName = metricName
    self.value = value
    self.timeStamp = timeStamp

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.clientMetricType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.metricName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.value = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.timeStamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MetricData')
    if self.clientMetricType is not None:
      oprot.writeFieldBegin('clientMetricType', TType.I32, 1)
      oprot.writeI32(self.clientMetricType)
      oprot.writeFieldEnd()
    if self.metricName is not None:
      oprot.writeFieldBegin('metricName', TType.STRING, 2)
      oprot.writeString(self.metricName)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.I64, 3)
      oprot.writeI64(self.value)
      oprot.writeFieldEnd()
    if self.timeStamp is not None:
      oprot.writeFieldBegin('timeStamp', TType.I64, 4)
      oprot.writeI64(self.timeStamp)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.clientMetricType)
    value = (value * 31) ^ hash(self.metricName)
    value = (value * 31) ^ hash(self.value)
    value = (value * 31) ^ hash(self.timeStamp)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ClientMetrics(object):
  """
  客户端用于传输metrics的数据结构

  Attributes:
   - metricDataList: 添加/获取客户端metrics数据
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'metricDataList', (TType.STRUCT,(MetricData, MetricData.thrift_spec)), None, ), # 1
  )

  def __init__(self, metricDataList=None,):
    self.metricDataList = metricDataList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.metricDataList = []
          (_etype21, _size18) = iprot.readListBegin()
          for _i22 in range(_size18):
            _elem23 = MetricData()
            _elem23.read(iprot)
            self.metricDataList.append(_elem23)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ClientMetrics')
    if self.metricDataList is not None:
      oprot.writeFieldBegin('metricDataList', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.metricDataList))
      for iter24 in self.metricDataList:
        iter24.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.metricDataList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class MetricQueryRequest(object):
  """
  统计指标查询请求

  Attributes:
   - tableName: 需要查询的表名
   - startTime: 起始时间，值为1970/0/0开始的秒数
   - stopTime: 结束时间，值为1970/0/0开始的秒数
   - metricKey: 统计指标主类型
   - metricType: 统计指标子类型
   - downsampleInterval: 下采样时间间隔, 0或者负数表示读取原始数据不进行下采样
   - downsampleTimeUnit: 下采样时间间隔单位
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tableName', None, None, ), # 1
    (2, TType.I64, 'startTime', None, None, ), # 2
    (3, TType.I64, 'stopTime', None, None, ), # 3
    (4, TType.I32, 'metricKey', None, None, ), # 4
    (5, TType.I32, 'metricType', None, None, ), # 5
    (6, TType.I32, 'downsampleInterval', None, None, ), # 6
    (7, TType.I32, 'downsampleTimeUnit', None, None, ), # 7
  )

  def __init__(self, tableName=None, startTime=None, stopTime=None, metricKey=None, metricType=None, downsampleInterval=None, downsampleTimeUnit=None,):
    self.tableName = tableName
    self.startTime = startTime
    self.stopTime = stopTime
    self.metricKey = metricKey
    self.metricType = metricType
    self.downsampleInterval = downsampleInterval
    self.downsampleTimeUnit = downsampleTimeUnit

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.tableName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.startTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.stopTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.metricKey = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.metricType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.downsampleInterval = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.downsampleTimeUnit = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MetricQueryRequest')
    if self.tableName is not None:
      oprot.writeFieldBegin('tableName', TType.STRING, 1)
      oprot.writeString(self.tableName)
      oprot.writeFieldEnd()
    if self.startTime is not None:
      oprot.writeFieldBegin('startTime', TType.I64, 2)
      oprot.writeI64(self.startTime)
      oprot.writeFieldEnd()
    if self.stopTime is not None:
      oprot.writeFieldBegin('stopTime', TType.I64, 3)
      oprot.writeI64(self.stopTime)
      oprot.writeFieldEnd()
    if self.metricKey is not None:
      oprot.writeFieldBegin('metricKey', TType.I32, 4)
      oprot.writeI32(self.metricKey)
      oprot.writeFieldEnd()
    if self.metricType is not None:
      oprot.writeFieldBegin('metricType', TType.I32, 5)
      oprot.writeI32(self.metricType)
      oprot.writeFieldEnd()
    if self.downsampleInterval is not None:
      oprot.writeFieldBegin('downsampleInterval', TType.I32, 6)
      oprot.writeI32(self.downsampleInterval)
      oprot.writeFieldEnd()
    if self.downsampleTimeUnit is not None:
      oprot.writeFieldBegin('downsampleTimeUnit', TType.I32, 7)
      oprot.writeI32(self.downsampleTimeUnit)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tableName)
    value = (value * 31) ^ hash(self.startTime)
    value = (value * 31) ^ hash(self.stopTime)
    value = (value * 31) ^ hash(self.metricKey)
    value = (value * 31) ^ hash(self.metricType)
    value = (value * 31) ^ hash(self.downsampleInterval)
    value = (value * 31) ^ hash(self.downsampleTimeUnit)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TimeSeriesData(object):
  """
  统计指标时间序列

  Attributes:
   - tableName: 表名
   - metricKey: 统计指标主类型
   - metricType: 统计指标子类型
   - data: 统计指标数据时间序列，值为{时间 => 数值}映射
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tableName', None, None, ), # 1
    (2, TType.I32, 'metricKey', None, None, ), # 2
    (3, TType.I32, 'metricType', None, None, ), # 3
    (4, TType.MAP, 'data', (TType.I64,None,TType.DOUBLE,None), None, ), # 4
  )

  def __init__(self, tableName=None, metricKey=None, metricType=None, data=None,):
    self.tableName = tableName
    self.metricKey = metricKey
    self.metricType = metricType
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.tableName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.metricKey = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.metricType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.data = {}
          (_ktype26, _vtype27, _size25 ) = iprot.readMapBegin()
          for _i29 in range(_size25):
            _key30 = iprot.readI64();
            _val31 = iprot.readDouble();
            self.data[_key30] = _val31
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TimeSeriesData')
    if self.tableName is not None:
      oprot.writeFieldBegin('tableName', TType.STRING, 1)
      oprot.writeString(self.tableName)
      oprot.writeFieldEnd()
    if self.metricKey is not None:
      oprot.writeFieldBegin('metricKey', TType.I32, 2)
      oprot.writeI32(self.metricKey)
      oprot.writeFieldEnd()
    if self.metricType is not None:
      oprot.writeFieldBegin('metricType', TType.I32, 3)
      oprot.writeI32(self.metricType)
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.MAP, 4)
      oprot.writeMapBegin(TType.I64, TType.DOUBLE, len(self.data))
      for kiter32,viter33 in list(self.data.items()):
        oprot.writeI64(kiter32)
        oprot.writeDouble(viter33)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tableName)
    value = (value * 31) ^ hash(self.metricKey)
    value = (value * 31) ^ hash(self.metricType)
    value = (value * 31) ^ hash(self.data)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Snapshot(object):
  """
  表快照

  Attributes:
   - snapshotName: 快照名
   - snapshotState: 快照状态
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'snapshotName', None, None, ), # 1
    (2, TType.I32, 'snapshotState', None, None, ), # 2
  )

  def __init__(self, snapshotName=None, snapshotState=None,):
    self.snapshotName = snapshotName
    self.snapshotState = snapshotState

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.snapshotName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.snapshotState = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Snapshot')
    if self.snapshotName is not None:
      oprot.writeFieldBegin('snapshotName', TType.STRING, 1)
      oprot.writeString(self.snapshotName)
      oprot.writeFieldEnd()
    if self.snapshotState is not None:
      oprot.writeFieldBegin('snapshotState', TType.I32, 2)
      oprot.writeI32(self.snapshotState)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.snapshotName)
    value = (value * 31) ^ hash(self.snapshotState)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TableSnapshots(object):
  """
  表的所有快照

  Attributes:
   - tableName: 表名
   - sysSnapshots: 系统自动生成的快照
   - userSnapshots: 用户生成的快照
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tableName', None, None, ), # 1
    (2, TType.LIST, 'sysSnapshots', (TType.STRUCT,(Snapshot, Snapshot.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'userSnapshots', (TType.STRUCT,(Snapshot, Snapshot.thrift_spec)), None, ), # 3
  )

  def __init__(self, tableName=None, sysSnapshots=None, userSnapshots=None,):
    self.tableName = tableName
    self.sysSnapshots = sysSnapshots
    self.userSnapshots = userSnapshots

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.tableName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.sysSnapshots = []
          (_etype37, _size34) = iprot.readListBegin()
          for _i38 in range(_size34):
            _elem39 = Snapshot()
            _elem39.read(iprot)
            self.sysSnapshots.append(_elem39)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.userSnapshots = []
          (_etype43, _size40) = iprot.readListBegin()
          for _i44 in range(_size40):
            _elem45 = Snapshot()
            _elem45.read(iprot)
            self.userSnapshots.append(_elem45)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TableSnapshots')
    if self.tableName is not None:
      oprot.writeFieldBegin('tableName', TType.STRING, 1)
      oprot.writeString(self.tableName)
      oprot.writeFieldEnd()
    if self.sysSnapshots is not None:
      oprot.writeFieldBegin('sysSnapshots', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.sysSnapshots))
      for iter46 in self.sysSnapshots:
        iter46.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.userSnapshots is not None:
      oprot.writeFieldBegin('userSnapshots', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.userSnapshots))
      for iter47 in self.userSnapshots:
        iter47.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tableName)
    value = (value * 31) ^ hash(self.sysSnapshots)
    value = (value * 31) ^ hash(self.userSnapshots)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SnapshotTableView(object):
  """
  存在快照的表视图

  Attributes:
   - tableName: 表名
   - tableExist: 表是否存在
   - deleteTime: 表的删除时间
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tableName', None, None, ), # 1
    (2, TType.BOOL, 'tableExist', None, None, ), # 2
    (3, TType.I64, 'deleteTime', None, None, ), # 3
  )

  def __init__(self, tableName=None, tableExist=None, deleteTime=None,):
    self.tableName = tableName
    self.tableExist = tableExist
    self.deleteTime = deleteTime

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.tableName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.tableExist = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.deleteTime = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SnapshotTableView')
    if self.tableName is not None:
      oprot.writeFieldBegin('tableName', TType.STRING, 1)
      oprot.writeString(self.tableName)
      oprot.writeFieldEnd()
    if self.tableExist is not None:
      oprot.writeFieldBegin('tableExist', TType.BOOL, 2)
      oprot.writeBool(self.tableExist)
      oprot.writeFieldEnd()
    if self.deleteTime is not None:
      oprot.writeFieldBegin('deleteTime', TType.I64, 3)
      oprot.writeI64(self.deleteTime)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tableName)
    value = (value * 31) ^ hash(self.tableExist)
    value = (value * 31) ^ hash(self.deleteTime)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class QuotaInfo(object):
  """
  Attributes:
   - accountId: 用户AccountId
   - tableNum: 表数量限制
   - tableNumUsed: 已存在表数量
   - space: 用户总的空间quota限制
   - spaceUsed: 已使用空间quota
   - readCapacity: 用户总的读quota限制
   - readCapacityUsed: 已使用读quota
   - writeCapacity: 用户总的写quota限制
   - writeCapacityUsed: 已使用写quota
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'accountId', None, None, ), # 1
    (2, TType.I32, 'tableNum', None, None, ), # 2
    (3, TType.I32, 'tableNumUsed', None, None, ), # 3
    (4, TType.I64, 'space', None, None, ), # 4
    (5, TType.I64, 'spaceUsed', None, None, ), # 5
    (6, TType.I64, 'readCapacity', None, None, ), # 6
    (7, TType.I64, 'readCapacityUsed', None, None, ), # 7
    (8, TType.I64, 'writeCapacity', None, None, ), # 8
    (9, TType.I64, 'writeCapacityUsed', None, None, ), # 9
  )

  def __init__(self, accountId=None, tableNum=None, tableNumUsed=None, space=None, spaceUsed=None, readCapacity=None, readCapacityUsed=None, writeCapacity=None, writeCapacityUsed=None,):
    self.accountId = accountId
    self.tableNum = tableNum
    self.tableNumUsed = tableNumUsed
    self.space = space
    self.spaceUsed = spaceUsed
    self.readCapacity = readCapacity
    self.readCapacityUsed = readCapacityUsed
    self.writeCapacity = writeCapacity
    self.writeCapacityUsed = writeCapacityUsed

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.accountId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.tableNum = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.tableNumUsed = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.space = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.spaceUsed = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.readCapacity = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.readCapacityUsed = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.writeCapacity = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.writeCapacityUsed = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('QuotaInfo')
    if self.accountId is not None:
      oprot.writeFieldBegin('accountId', TType.STRING, 1)
      oprot.writeString(self.accountId)
      oprot.writeFieldEnd()
    if self.tableNum is not None:
      oprot.writeFieldBegin('tableNum', TType.I32, 2)
      oprot.writeI32(self.tableNum)
      oprot.writeFieldEnd()
    if self.tableNumUsed is not None:
      oprot.writeFieldBegin('tableNumUsed', TType.I32, 3)
      oprot.writeI32(self.tableNumUsed)
      oprot.writeFieldEnd()
    if self.space is not None:
      oprot.writeFieldBegin('space', TType.I64, 4)
      oprot.writeI64(self.space)
      oprot.writeFieldEnd()
    if self.spaceUsed is not None:
      oprot.writeFieldBegin('spaceUsed', TType.I64, 5)
      oprot.writeI64(self.spaceUsed)
      oprot.writeFieldEnd()
    if self.readCapacity is not None:
      oprot.writeFieldBegin('readCapacity', TType.I64, 6)
      oprot.writeI64(self.readCapacity)
      oprot.writeFieldEnd()
    if self.readCapacityUsed is not None:
      oprot.writeFieldBegin('readCapacityUsed', TType.I64, 7)
      oprot.writeI64(self.readCapacityUsed)
      oprot.writeFieldEnd()
    if self.writeCapacity is not None:
      oprot.writeFieldBegin('writeCapacity', TType.I64, 8)
      oprot.writeI64(self.writeCapacity)
      oprot.writeFieldEnd()
    if self.writeCapacityUsed is not None:
      oprot.writeFieldBegin('writeCapacityUsed', TType.I64, 9)
      oprot.writeI64(self.writeCapacityUsed)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.accountId)
    value = (value * 31) ^ hash(self.tableNum)
    value = (value * 31) ^ hash(self.tableNumUsed)
    value = (value * 31) ^ hash(self.space)
    value = (value * 31) ^ hash(self.spaceUsed)
    value = (value * 31) ^ hash(self.readCapacity)
    value = (value * 31) ^ hash(self.readCapacityUsed)
    value = (value * 31) ^ hash(self.writeCapacity)
    value = (value * 31) ^ hash(self.writeCapacityUsed)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
