

Dict = {1: {'id':12345, 'first_name':'John', 'last_name':'Smith',
'assignments':[('assignment_1',1),('assignment_2',3),('assignment_3',0)]},
2: {'id':2468, 'first_name':'Mary', 'last_name':'Johnson',
'assignments':[('assignment_1',2),('assignment_2',2),('assignment_3',4)]},
3: {'id':3579, 'first_name':'Alex', 'last_name':'Henderson',
'assignments':[('assignment_1',4),('assignment_2',1),('assignment_3',3)]},
4: {'id':2345, 'first_name':'Jason', 'last_name':'Michaels',
'assignments':[('assignment_1',3),('assignment_2',3),('assignment_3',4)]}}

##average_grade of the students
def average_grade(students):
    total = 0
    count = 0
    for i in students.keys():
        for assignment_name, grade in students[i]['assignments']:
            total += grade
            count += 1
        
    return("The average grade for the students is " + str(total/count))


from collections import OrderedDict
from operator import itemgetter    


def highest_n_grades(students, assignment_name, n):
    scores_dict = {}

    for key in students.keys():
        the_id = students[key]['id']
        tuple_dict = dict(students[key]['assignments'])
        scores_dict[key] = (tuple_dict[assignment_name], the_id)
        

    scores_list = [x[1] for x in scores_dict.items()]
    scores_list = sorted(scores_list,key=lambda x:(-x[0],x[1]))
    return_list = scores_list[0:n]
    
    return_dict = {}
    return_ids = [x[1] for x in return_list]

    for key in students.keys():
        if students[key]['id'] in return_ids:
            return_dict[key] = students[key]
            
    return return_dict


#This function should accept a student dictionary, a string representing
#an assignment name and a grade. If that assignment name does not exist
#the assignment and grade should be added to the end of the list of assignments. If 
#this was successful it should return true, otherwise it should return false.

#what is student equivalent to? You have to refer to the dictionary.


student = Dict[1]

def add_grade(student, assignment_name, grade):
    newTuple = (assignment_name, grade)
    if newTuple in student['assignments']:
        return 'TRUE'
    else:
        print(newTuple)
        student['assignments'].append(newTuple)
        return 'FALSE'
            
    
#This function should accept a student dictionary, a string 
#representing an assignment name and a grade. If that assignment name exists
#the grade should be changed to the supplied grade. If the assignment was found
#and updated the function should return true, otherwise it should return false.
#The order of assignments should be preserved.

student = Dict[1]
assignment_name = 'assignment_1'
grade = 4

def update_grade(student, assignment_name, grade):
    mylist = list(student['assignments'])
    myDict = dict(mylist)
    if assignment_name in myDict:
      myDict[assignment_name] = grade
      newList = ([(k,v) for k, v in myDict.items()])
      student['assignments'] = newList
      return True
    else:
      return False



def passing_student_ids(students):
  result = []
  for i in students.keys():
    mylist = list(students[i]['assignments'])
    myDict = dict(mylist)
    if sum(myDict.values())/len(myDict) >= 2.0:
      result.append(students[i]['id']) 

  return(result)

            
            

 

 
