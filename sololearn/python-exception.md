## Exception Handling

    To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
    The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. If no error occurs, the code in the except block doesn't run.

## Multiple Exception Handling

    A try statement can have multiple different except blocks to handle different exceptions.
    Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.

## Finally

    To ensure some code runs no matter what errors occur, you can use a finally statement. The finally statement is placed at the bottom of a try/except statement. Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.

## Raise

    Raise allows you to throw an exception at any time.
    For example

    name = "123"
    raise NameError("Invalid name!")
