from django.db import models

# Create your models here.


class Departments(models.Model):
    name = models.CharField(max_length=20, verbose_name="部门名称", null=True, blank=True)

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Staffs(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名", null=True, blank=True)
    department = models.ForeignKey(Departments, null=True, blank=True, verbose_name="部门名称")

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=20, verbose_name="项目名", null=True, blank=True)
    staffs = models.ManyToManyField(Staffs)

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_all_staffs_name(self):
        return "\n".join([staff.name for staff in self.staffs.all()])
