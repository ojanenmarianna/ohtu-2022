*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  hello  world123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  hello123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  h  helloworld1
    Output should contain  Invalid username

Register With Valid Username And Too Short Password
    Input credentials  hello  w
    Output should contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input credentials  hello  worldabc
    Output should contain  Invalid password

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command