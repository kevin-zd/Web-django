from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
import json
# Create your views here.

# 1.先导入对应的模型
from . import models

class StudentView(View):
    def get1(self, request):
        """获取多个学生数据"""
        # 获取指定模型对应的数据表里面所在的数据记录
        """
        模型类名.objects.all()    # 获取模型对应的数据表的模型类对象
        """
        # object_list = models.Student.objects.all()[:5]
        # object_list = models.Student.objects.all()
        # print(type(object_list))
        # object_list = models.Student.objects.all()
        # """
        # QuerySet是django的 ORM中提供使用的查询集对象，支持使用索引来限制查询结果数量，但不支持使用负数索引
        # <class 'django.db.models.query.QuerySet'>
        # """

        # # 要获取单个模型对象
        # print('object获取的数据', object_list[0], type(object_list[0]))
        # student = object_list[0]
        # # 获取模型对象的字段属性
        # print(student.id, student.pk)  # 获取主键
        # print(student.name, student.description)   # 获取其他属性
        # print(student.created_time.strftime("%Y-%M-%D %H:%M:%S"))    # 获取日期格式的内容
        # 当字段声明中，使用choices可选值选项以后，在模型对象里面就可以通过get_<字段名>_display()来获取当前选项的文本提示
        # print(student.status, student.get_status_display())
        # return JsonResponse({})

        # # QuerySet里面的成员是模型数据，不能直接被json转换成数据，所以需要先转换对象为字典，然后经过json处理才可以给客户端
        # student_list = []
        # for object in object_list:
        #     student_list.append({
        #         "id": object.id,
        #         "name": object.name,
        #         "age": object.age,
        #         "sex": "女" if object.sex else "男",
        #         "status": object.get_status_display(),
        #         "classmate": object.classmate,
        #         "description": object.description
        #     })
            # print(object, type(object))

        """
        all()返回的是模型对象列表，如果要获取字典列表，则可以使用values()
        values()调用时没有传递参数，则默认获取所有字段内容

        使用values直接获取数据字典组成的列表数据
        """
        # student_list = models.Student.objects.values("id", "name")
        # student_list = models.Student.objects.values()
        # print(student_list)
        # return JsonResponse(student_list, safe=False)


        """
        get 获取符合查询条件的一条数据，如果获取不到则抛出 DoesNotExists异常，如果获取到符合的数据有多条也会抛出 MultipleObjectsReturned
        """
        # student = models.Student.objects.get(name="于心")
        # print(student, type(student))

        """
        如果获取不到则抛出，DoesNotExists异常 
        """
        # try:
        #     student = models.Student.objects.get(name="于心--")
        #     result = {
        #         "code": 0,
        #         "msg": "success",
        #         "data": {
        #             "id": student.id,
        #             "name": student.name,
        #             "age": student.age
        #         }
        #     }
        # except models.Student.DoesNotExist:
        #     result = {
        #         "code": -1,
        #         "msg": "does not exist",
        #         "data": {}
        #     }
        # return JsonResponse(result)
    
        """
        如果获取到符合条件的数据多条，也会报错
        """
        # try:
        #     student = models.Student.objects.get(name="小黄人1号")
        #     result = {
        #         "code": 0,
        #         "msg": "success",
        #         "data": {
        #             "id": student.id,
        #             "name": student.name,
        #             "age": student.age
        #         }
        #     }
        # except models.Student.MultipleObjectsReturned:
        #     result = {
        #         "code": -2,
        #         "msg": "multiple object returned!",
        #         "data": {}
        #     }
        # return JsonResponse(result)


        """
        get 在实际开发中，更多使用用于给开发者基于ID主键/唯一索引来获取一条数据
        """
        # try:
        #     # student = models.Student.objects.get(mobile="18516082024")    # 唯一索引
        #     student = models.Student.objects.get(id=10)    # 主键ID
        #     result = {
        #         "code": 0,
        #         "msg": "success",
        #         "data": {
        #             "id": student.id,
        #             "name": student.name,
        #             "age": student.age
        #         }
        #     }
        # except models.Student.DoesNotExist:
        #     result = {
        #         "code": -1,
        #         "msg": "does not exist",
        #         "data": {}
        #     }
        # return JsonResponse(result)

        """
        first 获取查询结果的第一条记录，如果查询数据不存在，则返回None
        """
        # student = models.Student.objects.first()
        # print(student, type(student))
        # # 基于条件过滤来获取符合条件的第一条
        # student = models.Student.objects.filter(name="小黄人1号").first()
        # print(student, type(student))
        # # 如果查询不到，返回None
        # student = models.Student.objects.filter(name="张三").first()
        # print(student, type(student))      # None <class 'NoneType'>
        # return JsonResponse({})

        """
        count 统计返回查询的结果集的数量，结果是一个数字
        """
        # student_objs = models.Student.objects.filter(classmate="306").all()
        # print(len(student_objs))
        # student_count = models.Student.objects.count()    # 统计全表的数据量
        student_count = models.Student.objects.filter(classmate="303").count()
        print(student_count)
        return JsonResponse({})

    
    def post(self, request):
        """添加数据"""
        # 1.接收客户端发送过来的数据
        data = json.loads(request.body)
        # 2.参数校验和格式转换

        # 3.模型操作：基于模型对象的save方法可以完成添加/更新操作
        """ 方法一：使用save方法添加数据 """
        # student = models.Student(
        #     name = data['name'],
        #     age = data['age'],
        #     sex = data['sex'],
        #     description = data['description'],
        #     mobile = data['mobile'],
        #     classmate=data['classmate'],
        #     status = data['status']
        # )
        # student.save()

        """ 方法二：使用create方法添加数据 """
        # student = models.Student.objects.create(
        #     name = data['name'],
        #     age = data['age'],
        #     sex = data['sex'],
        #     description = data['description'],
        #     mobile = data['mobile'],
        #     classmate=data['classmate'],
        #     status = data['status'] 
        # )

        # 4. 单条数据返回结果
        # data = {
        #     "id": student.id,
        #     "name": student.name
        # }

        """ 方法三：使用bulk_create批量创建多条数据 """
        stu1 = models.Student(name="小黄人1号", age=18, sex=True, status=0, classmate=301, mobile="18423456618", description="不怕不怕啦")
        stu2 = models.Student(name="小黄人2号", age=28, sex=False, status=0, classmate=201, mobile="18423456628", description="不怕不怕啦")
        stu3 = models.Student(name="小黄人3号", age=38, sex=True, status=0, classmate=303, mobile="18423456638", description="不怕不怕啦")
        stu4 = models.Student(name="小黄人4号", age=48, sex=True, status=0, classmate=303, mobile="18423456648", description="不怕不怕啦")


        # 4.返回结果
        # bulk_create的执行结果是成功添加到数据库的数据集对象QuerySet
        ret = models.Student.objects.bulk_create([stu1, stu2, stu3, stu4])
        print(ret)
        return JsonResponse(len(ret), status=201)
    
    # put
    def put(self, request):
        """更新数据"""

        """使用save保存当前模型数据，并同步到数据库(更新一条数据)"""
        # student = models.Student.objects.get(id=10)
        # # 对于查询出来的模型数据，可以修改一个或多个字段，只需要在最后使用save保存即可
        # student.name = "吴小杰"
        # student.save()

        """update 更新符合条件的一条或多条数据记录（更新多条数据）"""
        # student_objs = models.Student.objects.filter(id__in=[2,10]).all()   # 先获取数据
        # print(student_objs)
        # 例如，把id=2和id=10的2名学生同时安排到303班里面
        models.Student.objects.filter(id__in=[2,10]).update(classmate=303)

        return JsonResponse({})
    
    # delete
    def delete(self, request):
        """删除数据"""
        
        """
        模型对象.delete()   删除一条数据
        """
        # try: 
        #     student = models.Student.objects.get(id=24)
        #     student.delete()
        # except models.Student.DoesNotExist:
        #     pass

        """
        模型类.objects.delete()      删除全表数据！！！慎用！！！
        模型类.objects.filter(条件).delete()   删除符合条件的1条或多条数据
        """
        models.Student.objects.filter(id__gte=20).delete()

        return JsonResponse({})
    
    def get1(self, request):
        """过滤操作"""

        """
        相等运算符 exact 或者 = 
        推荐使用 =
        """
        # stu1 = models.Student.objects.filter(id=3).first()
        # stu2 = models.Student.objects.filter(id__exact=3).first()
        # print(stu1, type(stu1))
        # print(stu2, type(stu2))

        """ 
        startswith、endswith：以指定值开头或结尾
        模糊查询运算符，相当于SQL语句中的like
        模型类.objects.filter(字段名__contains="值")   # 表示查询包含指定值的数据，等价于SQL语句，字段名 like “%值%”
        模型类.objects.filter(字段名__startswith="值")   # 表示查询以指定值开头的数据，等价于SQL语句，字段名 like “值%”
        模型类.objects.filter(字段名__endswith="值")   # 表示查询以指定值结尾的数据，等价于SQL语句，字段名 like “%值”
        以上运算符都区分大小写，在这些运算符前加上i表示不区分字母大小写，如iexact、icontains、istartswith、iendswith

        """
        # 例如，查找所有名字中包含“华”字的学生信息
        # student_objs = models.Student.objects.filter(name__contains="华").all()
        # print(student_objs)

        # 例如，查询所有姓李的学生
        # student_objs = models.Student.objects.filter(name__startswith="王").all()
        # print(student_objs)

        # 例如，查询名字以“豪”字结尾的学生信息
        student_objs = models.Student.objects.filter(name__endswith="豪").all()
        print(student_objs)

        return JsonResponse({})
    

    def get2(self, request):
        """空查询"""
        student_objs = models.Student.objects.filter(description__isnull=True).all()
        print(student_objs)

        return JsonResponse({})
    
    def get3(self, request):
        """in 值范围查询/值列表查询"""
        # student_objs = models.Student.objects.filter(classmate__in=["305","306","307"]).all()
        # print(student_objs)

        """range 数字范围查询"""
        # 例如，查询出学号id在5～10之间的
        # student_objs = models.Student.objects.filter(id__range=(5, 10)).all()
        # print(student_objs)

        """
        比较查询
            = 或 exact  等于
            gt   大于
            gte  大于等于
            lt   小于
            lte  小于等于
        """
        # 小于
        # student_objs = models.Student.objects.filter(age__lt=24).all()
        # print(student_objs)

        # 小于等于
        # student_objs = models.Student.objects.filter(age__lte=24).all()
        # print(student_objs)

        # 大于
        student_objs = models.Student.objects.filter(age__gt=24).all()
        print(student_objs)

        return JsonResponse({})

    
    def get4(self, request):
        """时间查询"""
        # 查询添加数据时间为2025年的学生
        # student_objs = models.Student.objects.filter(created_time__year="2025").all()
        # print(student_objs)

        # 查询11月的学生
        # student_objs = models.Student.objects.filter(created_time__month="11").all()
        # print(student_objs)

        # 查询2025年10月的
        # student_objs = models.Student.objects.filter(created_time__year="2025", created_time__month="10").all()
        # print(student_objs)

        # 查询2025年11月20日
        # student_objs = models.Student.objects.filter(
        #     created_time__year="2025",
        #     created_time__month="11",
        #     created_time__day="20").all()
        # print(student_objs)
        

        # 查询11月20日
        # student_objs = models.Student.objects.filter(
        #     created_time__month="11",
        #     created_time__day="24").all()
        # print(student_objs)


        # 查询10:00的数据
        # student_objs = models.Student.objects.filter(
        #     created_time__hour="10").all()
        # print(student_objs)


        # 把字符串格式的时间转换成datetime对象，就可以查询
        # from django.utils.timezone import datetime
        # # 把字符串格式时间转换成datetime时间戳对象
        # timestamp = datetime.strptime("2025-10-20 22:11:24", "%Y-%m-%d %H:%M:%S")
        # student_objs = models.Student.objects.filter(created_time=timestamp).all()
        # print(student_objs)


        # 判断两个时间范围
        time1 = "2023-03-24 12:36:10"
        time2 = "2025-03-20 22:11:24"
        # 查询添加时间在time1与time2之间的数据
        student_objs = models.Student.objects.filter(
            created_time__gte=time1,
            created_time__lte=time2,
        ).all()
        print(student_objs)

        return JsonResponse({})


    def get5(self, request):
        """ F对象：实现字段与字段之间的判断过程 """
        # 查询添加数据以后没有被更新过的数据，要查询添加时间和更新时间保持一致的数据
        # select * from student where created_time = uptaded_time;
        from django.db.models import F 
        student_objs = models.Student.objects.filter(created_time=F("updated_time")).all()
        # print(student_objs)
        for student in student_objs:
            print(student, student.updated_time)

        return JsonResponse({})
    
    def get6(self, request):
        """ Q对象，用于实现多个条件之间的逻辑判断，类似SQL语句中and部分或者or部分内容 """
        # 例如，查询303班学生或者305班的数据
        # 再此之前，可以使用in来查询
        # student_objs = models.Student.objects.filter(classmate__in=["303","305"]).all()
        # print(student_objs)

        """使用Q对象实现查询"""
        # from django.db.models import Q
        # student_objs = models.Student.objects.filter(Q(classmate=303) | Q(classmate=305)).all()
        # print(student_objs)


        """使用Q对象实现更复杂的多条件关系 or 关系"""
        # from django.db.models import Q
        # student_objs = models.Student.objects.filter(Q(classmate="303", sex=1) | Q(classmate="305", sex=1)).all()
        # # select * from student where (class="301" and sex=1) or (class="302" and sex=1)
        # print(student_objs)

        """上面的语句可以简化"""
        # from django.db.models import Q
        # student_objs = models.Student.objects.filter(Q(classmate="303") | Q(classmate="305"), sex=1).all()
        # # select * from student where (class="301" and sex=1) or (class="302" and sex=1)
        # print(student_objs) 


        """and的实现，可以直接通过，逗号来实现"""
        # 查询307班年龄大于24的女生
        # student_objs = models.Student.objects.filter(classmate="307", sex=0, age__gt=24).all()
        # # select * from student where class="307" and sex=0 and age > 24
        # print(student_objs)

        # 查询307班年龄不等于24的女生
        from django.db.models import Q
        student_objs = models.Student.objects.filter(~Q(age=24), classmate="307", sex=0).all()
        print(student_objs)


        return JsonResponse({})
    
    def get7(self, request):
        """结果排序,order_by()
        升序(ASC）),数值从小到大
        降序(DESC),数值从大到小 

        单字段升序  order_by(“字段名”)
        单字段讲序  order_by("-字段名")

        多字段升序 order_by("字段名","字段名")     # 优先级从左往右
        """
        # 升序（ASC），数值从小到大
        # 降序（DESC），数值从大到小

        # 例如，查询出303班学生信息，并按年龄进行升序排序
        # student_objs = models.Student.objects.filter(classmate="303").order_by("age").values("id","name","age").all()
        # print(student_objs)
        

        # 例如，查询出303班学生信息，并按年龄进行降序排序
        # student_objs = models.Student.objects.filter(classmate="303").order_by("-age").values("id", "name", "age")
        # print(student_objs)

        # 例如，查询出303，305所有学生信息，并按班级进行升序排序，然后按年龄进行升序排序
        student_objs = models.Student.objects.filter(classmate__in=["303", "305", "307"]).order_by("classmate","age").values("id", "name", "classmate", "age")
        print(student_objs)

        return JsonResponse({})


    def get8(self, request):
        """
        查询集 QuerySet
        在django提供的ORM操作中，当使用all()获取查询结果时，返回值就是一个Query对象
        同时，在调用filter，exclude,order_by时，如果后面没有指定查询的查询结果方法，则这3个方法的内部会自动调用all()方法，返回的结果也是QuerySet
        """
        # 1.查询使用all()的情况
        # student_objs = models.Student.objects.filter(classmate="303").all()
        # print(student_objs)

        # # 2.使用filter或exclude 但是没有指定获取结果方法，默认是all()
        # student_objs = models.Student.objects.filter(classmate="303")
        # print(student_objs)

        # 3.使用order_by，但没有指定获取结果方法，默认也是all()
        student_objs = models.Student.objects.order_by("age").all()
        print(student_objs)

        student_objs = models.Student.objects.order_by("age")
        print(student_objs)


        return JsonResponse({})


    def get9(self, request):
        from django.db.models import Avg,Max,Min,Sum,Count
        """聚合查询"""
        # 例如，查询301班学生的平均年龄
        student_objs = models.Student.objects.filter(classmate="303").aggregate(Avg("age"))
        print(student_objs)

        # 最大
        student_objs = models.Student.objects.filter(classmate="303").aggregate(Max("age"))
        print(student_objs)


        # 数量
        # 例如，查询301班学生的平均年龄
        student_objs = models.Student.objects.filter(classmate="303").count()
        student_objs = models.Student.objects.filter(classmate="303").aggregate(Count("age"))

        print(student_objs)

        # 总计
        student_objs = models.Student.objects.filter(classmate="303").aggregate(Sum("age"))
        print(student_objs)

        return JsonResponse({})
    
    def get10(self, request):
        """聚合分组"""
    #    models.Student.objects.values("classmate").annotate(存储结果的变量=聚合函数（存储结果的变量=聚合函数（字段名））)
        # 例如，查询每一个班级的学生平均年龄
        from django.db.models import Avg
        # results = models.Student.objects.values("classmate").annotate(age_avg=Avg("age"))
        # print(results)

        """在分组之前使用filter过滤,filter相当于sql查询语句中的where"""
        # 例如，查询301，302，303的学生平均年龄
        # result = models.Student.objects.filter(classmate__in=["303", "305", "307"]).values("classmate").annotate(avg=Avg("age"))
        # print(result)


        """在分组之后使用filter过滤，filter相当于sql语句中的having"""
        # 例如，查询303，305，307的学生平均年龄大于20的班级
        result = models.Student.objects.filter(classmate__in=["303", "305", "307"]).values("classmate").annotate(avg=Avg("age")).filter(avg__gt=30)
        print(result) 

        return JsonResponse({})
    

    def get11(self, request):
        """ORM中的原生查询"""
        sql = "select * from student"
        student_objs = models.Student.objects.raw(sql)
        print(student_objs)
        for student in student_objs:
            print(student, type(student))


        return JsonResponse({})
    

    def get(self, request):
        """
        多库共存下，基于django底层安装的pymysql来使用原生SQL语句操作的切换数据连接，完成数据库查询的过程
        1.先到“demo/settings.py”里面，在databases配置项中新增一个数据库
        2.直接把school里面的school复制到students数据库
        create table students(

        )
        """
        # from django.db import connections
        # with connections["djdemo"].cursor() as cursor:
        #     # 让游标执行SQL语句
        #     cursor.execute("select * from student")
        #     # 通过游标获取查询结果
        #     result = cursor.fetchall()
        #     print(result)

        """ 多库共存下，基于django的ORM模型操作切换的数据连接 """
        # student_objs = models.Student.objects.using("djdemo").all()
        student_objs = models.Student.objects.using("default").values("name", "age")

        print(student_objs)
        # for student in student_objs:
        #     print(student)

        return JsonResponse({})

