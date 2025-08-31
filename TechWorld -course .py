
class TechWorld:
  # Contructor 
  def __init__(self):
    self.__name = None
    self.__technology_skills = []
    self.__experience = None
    self.__average_feedback = None

  # setter method 
  def set_name(self, name):
    self.__name = name
  def set_technology_skills(self, technology_skills):
    self.__technology_skills = technology_skills

  def set_experience(self, experience):
    self.__experience = experience

  def set_average_feedback(self, average_feedback):
    self.__average_feedback = average_feedback
  
# check eligibillity method 
  def check_eligibility(self):

    if self.__experience > 3 and self.__average_feedback >= 4.5:
      return True
    elif self.__experience <= 3 and self.__average_feedback >= 4:
      return True
    else:
      return False
# course allocate method 
  def allocate_course(self, technology):
    if technology in self.__technology_skills:
      return True
    else:
      return False

obj = TechWorld()
obj.set_name('Bhoopendra')
obj.set_experience(3)
obj.set_average_feedback(4)
obj.set_technology_skills(['python','sql','power BI'])
print(obj.check_eligibility())
print(obj.allocate_course('python'))
