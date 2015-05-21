from rest_framework import serializers

from drflab.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

    def create(self, validated_data):
        customer = Customer(**validated_data)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        return instance

class CustomerSerializerOverride(serializers.ModelSerializer):
    class Meta:
        model = Customer
    name = serializers.CharField()

    def validate(self, data):
        assert 'extra' not in data, data
        return data

    def create(self, validated_data):
        customer = Customer(**validated_data)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        return instance
