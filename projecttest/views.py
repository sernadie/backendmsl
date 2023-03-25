from django.shortcuts import render

# Create your views here.
import pandas as pd
import json
from rest_framework.response import Response
from rest_framework.views import APIView

def index_view(request):
    return render(request, "index.html")


class ExcelToJsonVW(APIView):
    template_name = "excel_to_json.html"

    def get(self, request):
        #Read excel
        df = pd.read_excel(r"C:\Matriz.xlsx", sheet_name="Hoja1")

        #DF to JSON
        json_output = df.to_json(orient="records")

        #Clean JSON to better reading
        json_output_clean = json.loads(json_output, parse_constant=None)

        #Return JSON to HTTP
        return Response(json_output_clean)
