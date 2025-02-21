from django.db import models

class  UserGroup(models.Model):
    group_name = models.CharField(max_length=255, unique=True)
    description = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.group_name
    

class  Employee(models.Model):
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name="employees")
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"
