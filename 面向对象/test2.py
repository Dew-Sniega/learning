
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   'ËùÓÐÑ§ÉúµÄ»ùÀà'
   stuCount = 0
   stu_count_wl163 = 0
   stu_count_wl161 = 0
   stu_count_male = 0
   stu_count_female = 0
 
   def __init__(self, stu_num,name, stu_class,gender):
      self.stu_num = stu_num
      self.name = name
      self.stu_class = stu_class
      self.gender = gender
      Student.stuCount += 1
      if self.stu_class == "wl163":
         Student.stu_count_wl163 += 1
      elif self.stu_class == "wl161":
         Student.stu_count_wl161 += 1
      if self.gender == "male":
         Student.stu_count_male += 1
      elif self.gender == "female":
         Student.stu_count_female += 1
   
   def displayCount(self):
     print "Total Student %d" % Student.stuCount

   def displayCountwl163(self):
     print "wl163 Student %d" % self.stu_count_wl163

   def displayCountwl161(self):
     print "wl161 Student %d" % self.stu_count_wl161

   def displayCountMale(self):
     print "Male Student %d" % self.stu_count_male

   def displayCountFemale(self):
     print "Female Student %d" % self.stu_count_female
 
   def displayStudent(self):
      print "Stu_num: ",self.stu_num,",Name : ", self.name,  ", Stu_class: ", self.stu_class,",Male: ",self.gender
      

     
