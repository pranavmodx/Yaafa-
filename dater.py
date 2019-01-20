import pandas as pd
import faker


fake=faker.Faker()

def student_names():
	a=[]
	for _ in range(50):
		a+=[fake.name()]
	return a

def create_id_name_pair():
	students=student_names()
	id=[]
	for i in range(50):
		id.append(hash(students[i]))
	df=pd.DataFrame(
		{'id':id,
		 'name':students,		
		})
	df.to_csv('master.csv',sep='\t',encoding='utf-8')

create_id_name_pair();
