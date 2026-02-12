# STORE VALUES

In [1]: from app10.models import Student

In [2]: Student.objects.all()
Out[2]: <QuerySet []>

In [3]: Student.objects.create(name = 'Muhammed', surname = 'chreiki', age = 22)
Out[3]: <Student: Student object (1)>

In [4]: Student.objects.all()
Out[4]: <QuerySet [<Student: Student object (1)>]>

In [5]: Student.objects.create(name = 'Yaser', surname = 'Ktifani', age = 21)
Out[5]: <Student: Student object (2)>

In [6]: Student.objects.all()
Out[6]: <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>

# GET VALUES CONVERT AND PRINT

In [1]: from app10.models import Student

In [2]: Student.objects.get(pk=2)
Out[2]: <Student: Student object (2)>

In [3]: student = Student.objects.get(pk=2)

## In [4]: keys = [key for key in student]

TypeError Traceback (most recent call last)
Cell In[4], line 1
----> 1 keys = [key for key in student]

TypeError: 'Student' object is not iterable

In [5]: pairs = [(k, v) for k, v in student.__dict__.items()]

In [6]: print(pairs)
[('_state', <django.db.models.base.ModelState object at 0x0000017A153D4410>), ('id', 2), ('name', 'Yaser'), ('surname', 'Ktifani'), ('age', 21)]

In [7]: fields = [field.name for field in student._meta.fields]

In [8]: print(fields)
['id', 'name', 'surname', 'age']

In [9]: data = {
...: field.name: getattr(student, field.name)
...: for field in student.\_meta.fields
...: }

In [10]: print(data)
{'id': 2, 'name': 'Yaser', 'surname': 'Ktifani', 'age': 21}

# Update Field

In [11]: student.name = 'Ahmed'

In [12]: student.save()

In [13]: Student.objects.all()
Out[13]: <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>

In [14]: print(data)
{'id': 2, 'name': 'Yaser', 'surname': 'Ktifani', 'age': 21}

In [15]: student = Student.objects.get(pk=2)

In [16]: data = {
...: field.name: getattr(student, field.name)
...: for field in student.\_meta.fields
...: }

In [17]: print(data)
{'id': 2, 'name': 'Ahmed', 'surname': 'Ktifani', 'age': 21}
