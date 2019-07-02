import json

# 此时student是一个dict格式内容，不是json
 student={

     "name":"wanghao",
     "age":18,
     "mobile":"1341616512"
 }

 print(type(student))

 stu_json = json.dumps(student)
 print(type(stu_json))

 print("JSon对象：{0}".format(stu_json))

 stu_dict = json.loads(stu_json)
 print(type(stu_dict))
 print(stu_dict)