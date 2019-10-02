#Copyright (c) 2019 42 Development dba 42 Electronics
#Author: Eric Feickert
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in the
#Software without restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

school  = {'students': [{'name': 'Annie', 'age': 11, 'score': 'A+'},
                       {'name':'Bobby', 'age': 13, 'score': 'B'},
                       {'name': 'Carla', 'age': 14, 'score': 'B-'},
                       {'name': 'David', 'age': 12, 'score': 'A'}],
           'teachers': [{'name': 'Mr B', 'subject': 'Math', 'grade': '6th'},
                       {'name': 'Mrs P', 'subject': 'Art', 'grade': '5th'}]}
school['students'].append({'name': 'Eric', 'age': 110, 'score': 'A'})

total_students = len(school['students'])
total_teachers = len(school['teachers'])



print('There are %s students' % total_students)
print('There are %s teachers' % total_teachers)

total_age = 0

for i in range(0, total_students):
    total_age = total_age + school['students'][i]['age']
av_age = total_age / total_students
print('Average student age is %s years old' % av_age)

