# Example: TestGroupBegin, TestGroupEnd

> Category: `Test` | Type: `notes`

## Description

Color usage

statements keywords comments test functions

MainTest()

{

// open first test group

TestGroupBegin("Test Mode Configuration", "Test cases concerning the build-in test mode.");

ConfigureSUT_Testmode(); // test cases of first test group

Toggle_Testmode();

SwitchOff_Testmode();

TestGroupEnd(); // end of first test group

// open second test group

TestGroupBegin("Management Functions", "Test cases concerning all management abilities.");

Check_ManagementFlag(); // test case is part of second test group

// open nested test group

TestGroupBegin("Power Management", "");

PowerUp(); // test cases of nested test group

PowerDown();

TestGroupEnd(); // end of nested test group

// open second nested test group

TestGroupBegin("Temperature Management", "");

NormalTemp(); // test cases of second nested test group

OverTemperature();

TestGroupEnd(); // end of second nested test group

TestGroupEnd(); // end of second test group

}
