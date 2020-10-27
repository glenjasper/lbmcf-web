from django.db import models

class Financer(models.Model):
    name = models.CharField(max_length = 15, verbose_name = 'Short name')
    full_name = models.CharField(max_length = 200, blank = True, verbose_name = 'Full name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Financer"
        verbose_name_plural = "Financers"
        ordering = ["name"]

    def __str__(self):
        return self.name

class AcademicDegree(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Academic Degree')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Academic Degree"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length = 200, verbose_name = 'Role name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    order = models.SmallIntegerField(verbose_name = 'Order', default = 0)
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 15, verbose_name = 'Short name')
    full_name = models.CharField(max_length = 200, blank = True, verbose_name = 'Full name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Country name')
    code = models.CharField(max_length = 5, verbose_name = 'Country code')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'State name')
    code = models.CharField(max_length = 5, verbose_name = 'State code')
    image = models.ImageField(upload_to = "states", verbose_name = "Flag", help_text = 'Please, the image must have the dimensions 500x350')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Institution(models.Model):
    short_name = models.CharField(max_length = 50, verbose_name = 'Short name')
    full_name = models.CharField(max_length = 200, verbose_name = 'Full name')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    country = models.ForeignKey(to = Country, on_delete = models.CASCADE, verbose_name = 'Country name')
    state = models.ForeignKey(to = State, on_delete = models.CASCADE, blank = True, null = True, verbose_name = 'State (Brazil)', help_text = 'Only for Brazil')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name

class GraduateProgram(models.Model):
    name = models.CharField(max_length = 15, verbose_name = 'Short name')
    full_name = models.CharField(max_length = 200, blank = True, verbose_name = 'Full name')
    institution = models.ForeignKey(to = Institution, on_delete = models.CASCADE, verbose_name = 'Institution')
    description = models.TextField(blank = True, verbose_name = 'Description', help_text = 'Description')
    status = models.BooleanField(default = True, verbose_name =  'Status')
    created = models.DateTimeField(auto_now_add = True, blank = True, null = True, verbose_name = 'Creation date')
    updated = models.DateTimeField(auto_now = True, blank = True, null = True, verbose_name = 'Modification date')

    class Meta:
        verbose_name = "Graduate Program"
        verbose_name_plural = "Graduate Programs"
        ordering = ["name"]

    def __str__(self):
        return self.name
