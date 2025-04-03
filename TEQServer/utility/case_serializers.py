from rest_framework import serializers


def snake_to_camel(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def camel_to_snake(camel_str):
    return "".join(["_" + c.lower() if c.isupper() else c for c in camel_str]).lstrip("_")

def to_representation(super, instance):
    ret = super.to_representation(instance)
    return {snake_to_camel(key): value for key, value in ret.items()}

def convert_keys_to_snake_case(data):
    if isinstance(data, dict):
        new_data = {}
        for key, value in data.items():
            new_key = camel_to_snake(key)
            new_data[new_key] = convert_keys_to_snake_case(value)
        return new_data
    elif isinstance(data, list):
        return [convert_keys_to_snake_case(item) for item in data]
    else:
        return data

def to_internal_value(super, data):
    snake_case_data = {camel_to_snake(key): value for key, value in data.items()}
    return super.to_internal_value(snake_case_data)

class CamelCaseModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return to_representation(super(), instance)

    def to_internal_value(self, data):
        return to_internal_value(super(), data)

    def get_snake_data(self):
        return convert_keys_to_snake_case(self.validated_data)


class CamelCaseSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return to_representation(super(), instance)

    def to_internal_value(self, data):
        return to_internal_value(super(), data)

    def get_snake_data(self):
        return convert_keys_to_snake_case(self.validated_data)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
