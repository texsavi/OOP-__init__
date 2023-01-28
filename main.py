
print("\033[36m")

class job:
  job=None
  salary=None
  hours=None
  dept=None
  speciality=None
  experience=None
  
  def __init__(self,job,salary,hours,dept,speciality,experience):
    self.job=job
    self.salary=salary
    self.hours=hours
    self.speciality=speciality
    self.dept=dept
    self.exp=experience
    
  def info(self):
    row=print(f"""Job: {self.job}\nSalary: {self.salary}\nHours Worked: {self.hours}\nSpeciality: {self.speciality}\nExperience: {self.exp}\nDept: {self.dept}""")
    print(row)
    
    
    
lawyer=job("Lawyer","$30K","100",None,None,None)
lawyer.info()
print()

class doctor(job):
  
 
  
  def __init__(self):
    self.job=job
    self.salary=salary
    self.hours=hours
    self.speciality=speciality 
    self.exp=experience
    
doctor=job("Doctor","$50k","80","Paeditrician","3",None)
doctor.info()
print()


class teacher(job):
  
  def __init__(self):
    self.job=job
    self.salary=salary
    self.hours=hours
    self.speciality=speciality
    self.dept=dept
      
teacher=job("Teacher","$90k","120","Comp Surgery","Comp Engience",None)  
teacher.info()
print()

  