from django.shortcuts import render
from api.user_data.userData import userData
from api.services.manipulationData import manipulationData
import io
from django.http import StreamingHttpResponse
import zipfile
# Create your views here.

def index(request):
    return render(request,"index.html")

"""
    API: user_data
    modified: 04/05/2025 | 01:31 PM
    describe: This api works on receiving data and preparing for other api/backend services.

"""
def user_data(request):
    # Request received from frontend
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=request.POST.get('nameSheet')
        # Apply the methods created in the API folder
        sheetNew = userData(sheet,typeSheet)
        sheetManipulation=manipulation_data_local(param=sheetNew)
        return sheetManipulation

"""
    service: manipulation_data_local
    modified: 04/05/2025 | 01:47 PM
    describe: This service function for api user-data.

"""

def manipulation_data_local(param):
        # Start manipulation data, class manipulationData.
        sheetManipulation = manipulationData(df=param)
        sheetManipulation.valueCell_isna()
        dfException = sheetManipulation.dataframe_expection()
        dfOutput = sheetManipulation.deletCell()

        # Makes a method that creates a package to download without needing to use database or alternative means.
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            buffer_output = io.BytesIO()
            buffer_except = io.BytesIO()

            dfOutput.to_excel(excel_writer=buffer_output, index=True)
            dfException.to_excel(excel_writer=buffer_except, index=True)

            buffer_output.seek(0)
            buffer_except.seek(0)

            zf.writestr("data_output.xlsx", buffer_output.read())
            zf.writestr("data_exception.xlsx", buffer_except.read())

        zip_buffer.seek(0)
        # Work on the http method to variable response return value pro frontend
        response = StreamingHttpResponse(
                zip_buffer,
        content_type="application/zip"
        )
        response['Content-Disposition'] = 'attachment; filename="data_compact.zip"'

        return response