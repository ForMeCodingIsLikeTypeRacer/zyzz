# Learning to test comprehensively, HW 2.

> DUE DATE: Feb 14 11:59PM

### Important notes: Do not try to modify any files/dirs other than "test".

## Set up
1. Make sure you installed both pytest,pytest-cov, and coverage.
2. Accept the Github classroom homework invitation.
3. In the root directory. Run  “pytest --cov --cov-report term-missing test”
4. This command will run the tests in the test/ directory, which test the files in the src/ directory. It will then generate a report of what tests passed, what failed, and then also which lines in the files in the src/ directory remain untested. These untested lines are a problem, because they might have defects. 
5. Look for  a table like this (among other things) in the coverage report. Your actual report might look a little different (in terms of the numbers). Note that we only care about coverage of the lines in the src/ directory (the Program Under Test). 

![](https://i.imgur.com/8Sd6gVZ.png)

Look at the columns indicating total lines, covered lines and missing lines (for example, the lines 35-37, line 50, and lines 63-57 in src/Admin.py are not covered; and then look at the tests and the code, and try and understand in a couple of cases why those lines are not covered by the tests. What we want you learn is here two things: a) How to improve coverage, and thus test a program more thoroughly; and b) how to write correct tests. 

---

## Overview of the project 
1. There are two source directories starting with “src” (code to be tested)  and “test” (the tests).
    - The files under “src”include inline-docs describing what the functions are supposed to be doing, **for the functions** in Admin.py, Student.py, and Instructor.py. These are the functions which will be the focus of your test. 
    - There are some undocumented functions elsewhere, we don’t care about testing them. They’re mostly utility functions used by the functions in the 3 well-documented files. Some of the functions in DataManager.py might be useful; for those functions, that you might need to use, there’s a Docstring in that file. The others do not have Docstring, and you shouldn’t need to use them.
    - There are some obvious (and some non-obvious) flaws in the code. This is intentionally intended to represent the usual kind of imperfect code that developers will refine via testing and debugging.  **Don’t be surprised if tests fail; failures will not affect your ability to achieve coverage and get full credit for this homework.**
    - **Please don’t fix bugs, or change, for any reason, any of the files in “src”. Think of yourself as playing the “tester” role; your job is just to learn how to write tests, someone else’s job is to fix the code. If you change the code, we may find that you have not achieved coverage, when we grade your tests, as submitted.** 

2. The  directory, test, contains the test files. Right now there  are just a few to get you started. You will be writing more.
    - The coverage is pretty low right now, when you use the command above (pytest… above) to run you will see what lines are covered, and what are missing.
    - You might get assertion failures, indicating a bug. A tester’s job is to find bugs. If you find failures, check and make sure your test logic is correct; if the tests are correct, and you found a real failure, that’s good. 
    - Write tests to increase coverage as much as possible in the 3 files: Admin.py, Student.py and Instructor.py. If you get to 100% you get full credit.
    - Next, look through the test case files for partially completed tests that describe what the tests are testing for, and complete them, by 1) Writing out all the calls and adding the statements to set up the test 2) Write the assertion to ensure that the correct behaviour is being checked.

3. The grading is based on two things: coverage (50%) and correctly written tests (50%)  that we asked for in the test case files.

---

## The Mechanics: Part 1
1. For each function in the 3 files above, examine the code, and try and figure out how to write tests that would drive the code into the parts that are not covered. Once you’ve got that, try and figure out what the right behaviour would be in that case, using the documentation
2. Once you have an idea of how to exercise them, and what the output/expected behaviour is, write the test. The test has 2 parts--calling the methods to execute the covered code, and then checking the right required state using an assert. 
3. Run the test, you should see increased coverage. 

## The Mechanics: Part 2 
In this part, you are required to complete test cases which we evaluate for correctness: we are checking that the test cases are correct, not the code. Be aware that tests are software, too, written by people, and can be wrong. A desired outcome for this course is that you learn to think about test case correctness. 

Look in each test case for test cases that we want you to complete. Think about how to set up the test as described, and what property should hold after the set up. Call the methods required for the setup, and save the values in local variables; then write the correct self.assert* statement over these variables. 

These test cases must precisely pass for the code we have given you and fail the incorrect code. We will be checking these test cases using correct version of the code under test (like the one you have been given) and also an incorrect version. **Your test should fail on the incorrect version, while passing on the correct one.**

## To turn in the homework:
1. Make sure you can connect to GitHub using ssh
2. Clone the repo
3. Start commiting changes on the main branch.
4. If you'd like to work on different branches, you will need to finally merge to main.

## Grading Policy:

1. If you achieve 100 percent statement coverage overall, across all files, you get 50% of the credit for this homework. If you get less (say yy% coverage overall) you get 50*(yy/xx)% credit.  This credit will be given in 5% steps, thus: 1-5% coverage, you get 2.5% of the credit, 5-10% coverage, 5% of the credit, and so on.

3. The other 50% is based on test cases that we have asked you to write. The credit is split equally across these required test cases. You get credit for a test case if it passes on the correct version, and fails on the wrong version. There is no partial credit for this part.

---

## What is this?

This is a project reflecting some code to manage enrollment that has a partial test set

## What should I do

Add more test cases, to achieve more coverage. Your grade will be based on how
much coverage you can achieve.

## How to measure coverage

Use conda to install pytest, and then try

```bash
pytest --cov src/
```

## How to increase coverage

Just add more tests! Look at the test/test_all.py file to see
a sample. Then, read through the source code in the src/ directory,
to get an idea of which parts of the code needs to get tested and add more
tests.

## What if a test fails

Well, that means you're a good tester! Rejoice, and then go on and write
more tests to increase coverage.


---

© Prem Devanbu. All rights reserved. Violators will be pursued to the fullest extent of the law. 
