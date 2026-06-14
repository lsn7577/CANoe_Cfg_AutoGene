# TestReportAddEngineerInfo, TestReportAddSetupInfo, TestReportAddSUTInfo

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddEngineerInfo (char name[], char description[], ...);
```

## Description

With these functions, information pairs of name and description (e.g. "serial number" and "S012345AB") can be taken up into the report in the areas TestEngineer, TestSetUp, and device (SUT) to be tested. The three areas named must not be created; they are automatically available in the report. In the course of the test execution, any number of information pairs can be written.

## Return Values

—

## Availability

| Since Version |
|---|
