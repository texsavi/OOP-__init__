# 👉 Day 64 Challenge

In today's project, create classes to represent jobs.

Your program should

1. Create a generic 'job' class.
2. The init method will store the details for name, salary and hours worked.
3. 'job' will have another method that prints those details nicely.
4. Create two sub-classes from job: 'doctor' and 'teacher'
5. The 'doctor' subclass should also include 'speciality' and 'years of experience'. 
6. The 'teacher' subclass should also include 'subject' and 'position'.
7. The print functions for each sub-class should print this extra data.
8. Instantiate a lawyer, a computer science teacher, and a pediatric doctor (this is a doctor for children) with 7 years of experience.
9. Output the information for each job.


Example:

```
🌟Jobs Jobs Jobs!🌟

Job type: Lawyer
Salary: $ Squillions
Hours worked: 60

Job type: Teacher
Salary: $ Nowhere near enough
Hours worked: All of them
Subject: Computer Science
Position: Classroom Teacher

Job type: Doctor
Salary: $ Doing very nicely thank you
Hours worked: 50
Speciality: Pediatric Consultant
Years of Experience: 7
```

<details> <summary> 💡 Hints </summary>
  
- Copy the `print` method to each of your sub-classes and customize it for each one.
- Don't worry about keeping the same method name. The one in the sub-class will override the one in the 'job' main class.

</details>