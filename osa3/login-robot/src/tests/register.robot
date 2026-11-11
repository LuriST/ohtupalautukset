*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  matti  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  matti  salasana123
    Input New Command
    Input Credentials  matti  salasana456
    Output Should Contain  User with username matti already exists

Register With Too Short Username
    Input New Command
    Input Credentials  ab  salasana123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  Matti  salasana123
    Output Should Contain  Username must contain only lowercase letters

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  pekka  sala12
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  ville  salasanapitka
    Output Should Contain  Password must contain characters other than letters