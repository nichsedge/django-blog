# Create your models here.

'''
class Akun(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.name
'''
