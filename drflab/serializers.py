from rest_framework import serializers

from drflab.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer

    def create(self, validated_data):
        import pdb;pdb.set_trace()
        customer = Customer(**validated_data)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        return instance
