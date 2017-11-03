
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stuCount = 0
 
   def __init__(self, stu_num,name, stu_class,male):
      self.stu_num = stu_num
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1
   
   def displayCount(self):
     print "Total Student %d" % Student.stuCount
 
   def displayStudent(self):
      print "Stu_num: ",self.stu_num,",Name : ", self.name,  ", Stu_class: ", self.stu_class,",Male: ",self.male
