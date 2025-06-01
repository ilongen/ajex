import pandas as pd
import io
import zipfile

from django.http import StreamingHttpResponse


class ManipulationData:
    def __init__(self,df):
        self.df=df
        self.df_backup = None
        self.n_row,self.n_columns = self.df.shape
        self.listDictNA = []
        self.listnot_na=[]
        self.list_rowExcept=[]
        self.rowDelet = []

    def value_cells_isnan(self):
        for i in range(self.n_row):
            for j in range(self.n_columns):
                value=self.df.iloc[i,j]
                try:
                    if pd.isna(value):
                        self.listDictNA.append({"row": i, "column": j})
                        if i not in self.list_rowExcept:
                            self.list_rowExcept.append(i)
                    else:
                        self.listnot_na.append({"row": i, "column": j, "value": value})
                except:
                    print("ERROR")
                finally:
                    print("SUCCESS SEPARATED VALUE IS NA")
        return self.listDictNA
    
    def delet_cell(self):
        porc_column_min = self.n_columns * 0.02
        count_row=0
        row_now = None
        for item in self.listDictNA:
            row=item["row"]
            if row != row_now:
                row_now=row
                count_row=0
            count_row +=1
            if count_row >= porc_column_min and row not in self.rowDelet:
                self.rowDelet.append(row)
        self.df.drop(index=self.rowDelet,inplace=True)
        return self.df
    
    def dataframe_exception(self):
        valid_indices = [i for i in self.list_rowExcept if i < len(self.df)]
        self.df_backup = self.df.iloc[valid_indices]
        return self.df_backup

    def download_zip(self):
        # Makes a method that creates a package to download without needing to use database or alternative means.
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            buffer_output = io.BytesIO()
            buffer_except = io.BytesIO()

            self.df.to_excel(excel_writer=buffer_output, index=True)
            self.df_backup.to_excel(excel_writer=buffer_except, index=True)

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