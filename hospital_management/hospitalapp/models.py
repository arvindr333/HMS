from django.db import models

class dept(models.Model):
    dept_name = models.CharField(max_length=225)
    dep_desc = models.TextField()

    def __str__(self):
        return self.dept_name


class Doctor(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    department = models.ForeignKey(dept, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors', null=True, blank=True)

    def __str__(self):
        return self.doc_name + " - " + self.doc_spec


class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booked_on = models.DateField()

    def __str__(self):
        return f"{self.p_name} - {self.doc_name}"

