from rest_framework.decorators import api_view
from prediction.validate.validation import validation
from prediction.prepareInputFile.prepareInputFile import prepareDataFile
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(["POST"])
def train_model(request):
    # print(validation.call())
    print(prepareDataFile.get_data())
    return Response("Training started")