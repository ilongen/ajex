from django.http import JsonResponse


class SignIn:
    """
        TODO:
        Fazer a criação da api pelo django rest, tentar criar pelo menos o caminho
    """
    def __int__(self):
        self.email = ''
        self.password = ''
        self.username = ''
    def sign_in(self):
        email = self.email.strip()
        password = self.password.strip()
        username = self.username.strip()
        return email,password,username
    def rules(self):
        password = self.password
        length = len(password)
        if length < 6:
            JsonResponse({"status":"failed","message":"Password must be at least 8 characters"})
        else:
            JsonResponse({"status":"success"})
        email = self.email
        length = len(email)
        if length < 50:
            JsonResponse({"status":"failed","message":"Email must be at least 50 characters"})
        else:
            JsonResponse({"status":"success"})