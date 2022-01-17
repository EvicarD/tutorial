from employee import Employee, EmployeeTest, Employer

ep_1 = Employee()
ep_2 = Employee()

ep_1.name = "ed"
ep_1.occupation = "developer"
ep_2.name = "bayka"
ep_2.occupation = "developer"

ep_test_1 = EmployeeTest("ed", "frontend", "ed@gmail.com", 10000)
ep_test_2 = EmployeeTest("bayka", "backend", "bayka@gmail.com", 10000)

print(ep_1.name)
print(ep_2.name)

print(ep_test_1.occupation)
ep_test_1.raise_amount = 1.1
print(ep_test_1.raise_amount)
ep_test_1.salary_raise()
print(ep_test_1.salary)



print(ep_test_2.occupation)
print(ep_test_2.raise_amount)
ep_test_2.salary_raise()
print(ep_test_2.salary)

print(str(ep_test_1))
print(str(ep_test_2))

print(f"number of employees: {EmployeeTest.number_of_employee}")

print(__name__)


employer = Employer("ed", "frontend", "ed@gmail.com", 10000, "vitz")
print(employer.car)