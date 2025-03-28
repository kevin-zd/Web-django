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
    
    def get(self, request):
        """过滤操作"""

        """
        相等运算符 exact 或者 = 
        """
        stu1 = models.Student.objects.filter(id=3).first()
        stu2 = models.Student.objects.filter(id__exact=3).first()
        print(stu1, type(stu1))
        print(stu2, type(stu2))
        return JsonResponse({})


