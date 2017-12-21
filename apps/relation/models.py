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

# ---------------------------------------------测试through----------------------------------------------------------


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Gloup(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    """
    on_delete有:
    CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
    PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
    SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)    # models.CASCADE 级联删除
    group = models.ForeignKey(Gloup, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
