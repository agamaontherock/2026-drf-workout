from rest_framework import serializers
from .models import Book, BookGenre
from decimal import Decimal



class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ["name", "slug"]


# class BookGenreSeria
class BookModelSerializer(serializers.ModelSerializer):
    price_vat = serializers.SerializerMethodField()
    # genre = serializers.StringRelatedField()
    genre = BookGenreSerializer()
    class Meta:
        model = Book
        fields = ["title", "author", "inventory", "price", "price_vat", "genre"]
        
        
    def get_price_vat(self, obj):
        return Decimal(1.2) * obj.price
    

