
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stuCount = 0
 
   def __init__(self, stu_num,name, stu_class,sex):
      self.stu_num = stu_num
      self.name = name
      self.stu_class = stu_class
      self.sex = sex
      Student.stuCount += 1
   
   def displayCount(self):
      print "Total Student %d" % Student.stuCount
 
   def displayStudent(self):
      print "Stu_num: ",self.stu_num,",Name : ", self.name,  ", Stu_class: ", self.stu_class,",Sex: ",self.sex


class Pupil(Student):
   canRecite_num = 0
   canOral_num = 0
   
   def __init__(self,skill):
      self.skill = skill
      if self.skill == "recite":
         Pupil.canRecite_num += 1
      elif self.skill =="oral":
         Pupil.canOral_num += 1
         

   def displaycanRecite(self):
      print "Student num: ",self.canRecite_num

   def displaycanOral(self):
      print "Student num: ",self.canOral_num


class Middleschstu(Student):
   canChemistry_num = 0
   canPhyscis_num = 0

   def __init__(self,skill):
      self.skill = skill
      if self.skill == "chemistry":
         Middleschstu.canChemistry_num += 1
      elif self.skill == "physcis":
         Middleschstu.canPhyscis_num += 1

   def displaycanChemistry(self):
       print "Student num: ",self.canChemistry_num

   def displaycanPhysics(self):
       print "Student num: ",self.canPhyscis_num

     
