*** Settings ***
Resource  resource.robot

*** Test Cases ***
Reset Counter After Increase
    Counter Value Should Be  0
    Increase Counter
    Counter Value Should Be  1
    Reset Counter
    Counter Value Should Be  0