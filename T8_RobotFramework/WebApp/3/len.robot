*** Settings ***
Documentation    Test for len function
Library    OperatingSystem
Suite Setup    Initialize Global Variables    # Initialize global variables for the test suite

*** Variables ***

${num1}    5
${num2}    8
${USER}    ${EMPTY}    # Get the current user from the environment variable

*** Test Cases ***

String Length Test
    [Documentation]    Test to check the length of a string
    ${string}=    Set Variable    Hello, World!    # Define a string variable
    ${length}=    Evaluate    len("${string}")    # Calculate the length of the string
    Should Be Equal As Integers    ${length}    13    # Check if the length is equal to 13
    Log   Length of the string: ${length}    console=True

Calculation Test
    [Documentation]    Test to check a calculation result
    ${result}=    Addition    ${num1}    ${num2}
    Should Be Equal As Numbers    ${result}    13    # Check if the addition of num1 and num2 equals 13

Greeting Test
    [Documentation]    Test to greet the user
    ${greeting}=    Say Hello    # Call the Say Hello keyword with the current user
    Should Be Equal    ${greeting}    Hello, ensei!    # Check if the greeting is correct

*** Keywords ***

Initialize Global Variables
    [Documentation]    Initialize global variables for the test
    ${USER}=    Get Environment Variable    USERNAME    # Set the user variable to the environment variable value
    Set Global Variable    ${USER}    ${USER}    # Set the global variable for the user
    Log   Current user: ${USER}    console=True

Addition
    [Arguments]    ${num1}    ${num2}
    ${result}=    Evaluate    ${num1} + ${num2}
    [Return]    ${result}
    Log    Result of addition: ${result}    console=True

Say Hello
    ${greeting}=    Set Variable    Hello, ${USER}!
    Log    ${greeting}    console=True
    [Return]    ${greeting}