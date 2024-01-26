from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our api """
    name = serializers.CharField(max_length=10)
