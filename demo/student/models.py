from django.db import models

"""
1.django中所有的模型，必须直接或间接继承models.Model模型基类
"""
class BaseModel(models.Model):
    # auto_noew_add：设置当前字段会在新建数据时，把当前时间戳作为默认值保存到当前字段中
    created_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建时间")
    # auto_now：设置更新数据时，把当前时间戳作为默认值保存到当前字段中
    updated_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间") 

    class Meta:
        # 设置当前类为抽象模型，表示当前模型并不是一个真正的表，django就不会跟踪识别这个模型了
        abstract = True

"""
create table 'student' {
    name varchar(15),
    key name(name)
    age smallint,
    sex tinyint default 1,
    class varchar(50) default "",
    key class(class),
    mobile varchar(20),
    unique key mobile(mobile)
    description text,
    status int default 1

}
"""
# Create your models here.
class Student(BaseModel):
    STATUS = (
        # (数据库值， “程序显示给外界看的文本”)，   # 模型对象.get_字段名_display()获取提示文本
        (1, "正常"),
        (2, "未入学"),
        (3, "已毕业")
    )
    # django模型中不需要单独声明主键，模型会自动创建主键ID，可以通过模型对象.id，或者模型对象.pk就可以直接调用主键
    name = models.CharField(max_length=15,db_index=True, verbose_name="姓名")
    age = models.SmallIntegerField(default=0, verbose_name="年龄")
    sex = models.BooleanField(default=True, verbose_name="性别")
    classmate = models.CharField(max_length=50, db_column="class", default="", db_index=True, verbose_name="班级编号")
    mobile = models.CharField(max_length=20, unique=True, verbose_name="手机号码")
    description = models.TextField(blank=True, null=True, verbose_name="个性签名")
    status = models.IntegerField(choices=STATUS, default=1, null=True, verbose_name="毕业状态")


    class Meta:
        db_table = "student"
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    # 当使用print打印Django模型对象时输出内容，返回值必须是字符串，方法名固定
    def __str__(self):
        # 当使用print打印django模型对象时的输出内容，返回值必须是字符串，方法名固定
        return self.name