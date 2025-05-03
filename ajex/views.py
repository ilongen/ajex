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
    modified: 26/04/2025 | 09:42 PM
    describe: This api works on receiving data and preparing for other api/backend services.

"""
def user_data(request):
    if request.method == "POST":
        sheet=request.FILES.get('fileSheet')
        typeSheet=request.POST.get('nameSheet')
        sheetNew = userData(sheet,typeSheet)
        sheetManipulation=manipulation_data_local(param=sheetNew)
        return sheetManipulation
    
def manipulation_data_local(param):
        sheetManipulation = manipulationData(df=param)
        sheetManipulation.valueCell_isna()
        dfException = sheetManipulation.dataframe_expection()
        dfOutput = sheetManipulation.deletCell()
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

        response = StreamingHttpResponse(
                zip_buffer,
        content_type="application/zip"
        )
        response['Content-Disposition'] = 'attachment; filename="data_compact.zip"'

        return response