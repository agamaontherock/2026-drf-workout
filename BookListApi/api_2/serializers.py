from rest_framework import serializers
from .models import Book, BookGenre
from decimal import Decimal

# class BookGenreSeria
class BookModelSerializer(serializers.ModelSerializer):
    price_vat = serializers.SerializerMethodField()
    genre = serializers.HyperlinkedRelatedField(view_name = "genre-detail", read_only = True)
    class Meta:
        model = Book
        fields = ["title", "author", "inventory", "price", "price_vat", "genre"]

    def get_price_vat(self, obj):
        return Decimal(1.2) * obj.price
        

class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = ["name"]
        
    