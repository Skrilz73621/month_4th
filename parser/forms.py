from . import models, parser
from django import forms

class ParserForm(forms.Form):
   
    def parser_data(self):
        parsed_book = parser.parsing()
        for i in parsed_book:
            models.BookParser.objects.create(**i)