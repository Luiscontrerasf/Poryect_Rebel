#from django.db import models
#from django.contrib.auth.models import BaseUserManager

#class UserManager(BaseUserManager, models.Manager):

 #       def create_user(self, username, pasword, is_staff, is_superuser):
  #          user = self.model(
   #             username = username                
    #            is_staff=is_staff
     #           is_superuser = is_superuser
      #      )
       #     user.set_password(pasword)
        #    user.save(using=self.db)
         #   return user
        
        #def create_superuser(self, usename, pasword=None,)
         #   return self._create_user(username, pasword, True , True)
