from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()


class EmailBackend(object):
   def authenticate(self, request, *args, **kwargs):
      try:
         email = kwargs["email" if "email" in kwargs else "username"]
         password = kwargs["password"]

         user = UserModel.objects.get(Q(email=email) | Q(username=email))

         if user.check_password(password):
            return user
      except UserModel.DoesNotExist:
         pass

      return None


   def get_user(self, pk):
      try:
         return UserModel.objects.get(pk=pk)
      except UserModel.DoesNotExist:
         return None
