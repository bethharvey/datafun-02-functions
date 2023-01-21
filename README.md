# datafun-02-functions

> Practice with built-in functions, creating functions, creating methods (functions in a class), and employing statistical functions

## Prerequisite

1. Complete the steps at [datafun-01-getting-started](https://github.com/denisecase/datafun-01-getting-started).
1. Get the authors code as described at [datafun-01-textbook](https://github.com/denisecase/datafun-01-textbook).

See those projects for additional help with tasks below. 

## Goals

1. Use built-in functions.
1. Create and call custom functions.
1. Create methods (functions in a class)
1. Employ statistical functions

## Task 1 - Fork this Repo

Fork this repo into your GitHub account.

## Task 2 - Clone Your Repo 

Clone your new repo down to your machine.

## Task 3 - Open the Project Locally

Open the project in VS Code. 

## Beth's Notes:
To use doctest on a class, create an instance of the class in
doctest format with the desired arguments: 
>>> ClassName(keyword=arguments)
Next, call the desired class method, followed by the expected output:
>>> ClassName.method()
Expected output
- Example in useroop.py

To call a class method (method1) within a different method (method2) in the same class:
def method2(self):
    self.method1()
- Example in useroop.py