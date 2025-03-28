""" 自定义路由转换器 """
from django.urls.converters import StringConverter, register_converter
class MobileConverters(StringConverter):
    regex = "1[3-9]\d{9}"

register_converter(MobileConverters, "mob")