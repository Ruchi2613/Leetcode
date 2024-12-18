# import typer
# #
# #
# # def main(name: str):
# #     print(f"Hello {name}")
# #
# # def funct(age: int,name:str):
# #     print(f"Hello {age},{name}")
# #
# #
# # if __name__ == "__main__":
# #     typer.run(funct)
#
#
# # class typer_cli:
# #
# #     def funct1(self,name:str):
# #         print(f" Hello {name}")
# #
# #     def funct2(self,name:str,age:int):
# #         print(f" Helloo {name} {age}")
# #
# #     def funct3(self,name:str,age:int):
# #         self.funct1(name)
# #         self.funct2(name,age)
# #
# # cli = typer_cli()
# #
# # def main(name: str, age: int):
# #     cli.funct3(name, age)
# #
# # if __name__ == "__main__":
# #     typer.run(main)
#
#
#
# app = typer.Typer()
#
# @app.command()
#
# def create(customer:str):
#     print(f"Hello {customer}")
#
# def cancel(customer:str):
#     print(f"Hello {customer}")
#
# if __name__ == "__main__":
#     app()

# I refer this video but I wrote code on my own:
'''https://www.youtube.com/watch?v=f7eQ2lQv-NI
 and for JSON i used this link:

 https://www.google.com/search?q=how+to+store+and+read+list+of+data+in+json+file+using+python&sca_esv=427fd9fc564ca397&sxsrf=ADLYWII7ZQ7u2u-9Tl0clsbQLDOwlGgUHg%3A1733263977736&ei=aYJPZ4XULJOC0PEPqpnc4AQ&ved=0ahUKEwjFrMe9z4yKAxUTATQIHaoMF0wQ4dUDCA8&uact=5&oq=how+to+store+and+read+list+of+data+in+json+file+using+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiPGhvdyB0byBzdG9yZSBhbmQgcmVhZCBsaXN0IG9mIGRhdGEgaW4ganNvbiBmaWxlIHVzaW5nIHB5dGhvbjIFEAAY7wUyCBAAGKIEGIkFMggQABiABBiiBDIFEAAY7wVIlEFQtQlY7zRwBngBkAEAmAFfoAHFB6oBAjEzuAEDyAEA-AEBmAIMoAKHBsICChAAGLADGNYEGEfCAgcQIxgnGK4CwgIKECEYoAEYwwQYCsICCBAhGKABGMMEmAMAiAYBkAYIkgcCMTKgB_0-&sclient=gws-wiz-serp
'''

import argparse
import os
import json

print(f"Hello from Task-Manager!!!")
print(end='\n')
tasks_file = "tasks.json"

if os.path.exists(tasks_file):
    with open(tasks_file,"r") as f:
        tasks = json.load(f)
else:
    tasks = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Hello from Task Manager!'
    )

    parser.add_argument('task', nargs='?', help="Specify the task")  # 'task' is optional for list operation
    parser.add_argument('operation', help="select operations")
    # args = parser.parse_args(["Write Code", "add"])
    # print(args.task)  # Output: Write Code
    # print(args.operation)  # Output: add
    args = parser.parse_args()
    print(args)

    # suppose, if I passed 'python typer_cli.py "Complete Homework" "add"' into terminal then it shows :
    # Namespace(task='Complete Homework', operation='add') : Namespace meaning: in python namespace used as a container to --
    # to store the value or attribute(properties). eg: args.task and args.operation are attributes of the namespace object returned by parser.parse_args().

    if args.operation == "add":
        if args.task is not None:
            task_lower = args.task.lower()
            if task_lower not in tasks:
                tasks.append(task_lower)
                print(f"Task '{args.task}' has been added!")
            else:
                print(f"Error:Task '{args.task}' is already in the list.")
        else:
            print("Error: Task description is required for 'add' operation.")

    elif args.operation == "remove":
        if args.task in tasks:
            tasks.remove(args.task)
            print(f"Task '{args.task}' has been removed!")
        else:
            print(f"Error:Task '{args.task}' are not in the list.")
    elif args.operation == "list":
        if tasks is not None:
            print("Here are your tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks available.")
    elif args.operation == 'update': # I'm sorry: for this I used CHATGPT but I understood the concept.
        if tasks is not None:
            if args.task is not None and args.task in tasks:
                new_task = input("Enter the updated task description: ")
                index = tasks.index(args.task)
                tasks[index] = new_task
                print(f"Task '{args.task}' updated to '{new_task}'.")
            else:
                print(f"Error: Task '{args.task}' not found")

    else:
        print(f"Error:{args.operation} is not valid for this task.Please use any of this operations like: add, remove, list and update.")


    with open(tasks_file, "w") as f:
        json.dump(tasks, f)


