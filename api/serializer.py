from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from api.models import User
class UserModelSerializer(ModelSerializer):
    """序列化器与反序列化器整合"""

    class Meta:
        model = User
        # 字段应该写哪些  应该写参与序列化与反序列化的并集
        fields = ("username", "password")

        # 添加DRF官方所提供的校验规则
        extra_kwargs = {
            "username": {
                "required": True,  # 设置为必填项
                "min_length": 2,  # 最小长度
                "error_messages": {
                    "required": "名字必填",
                    "min_length": "名字太短"
                }
            },
            "password": {
                "required": True,
                "min_length": 6,
                "error_messages": {
                    "required": "密码必填",
                    "min_length": "密码太短"
                }
            },
        }

    def validate_username(self, value):

        request = self.context.get('request')
        print(request)
        book = User.objects.filter(username=value)
        if book:
            raise exceptions.ValidationError("用户已存在")
        return value

class UserModelSerializer2(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        # 添加DRF官方提供的规则
        extra_kwargs = {
            "username": {
                "required": True,  # 设置为必填项
                "error_messages": {
                    "required": "用户名必须填写",
                }
            },
            "password": {
                "required": True,
                "error_messages": {
                    "required": "密码必须填写",
                }
            },
        }