# TestStep, TestStepPass, TestStepFail, TestStepWarning, TestStepInconclusive, TestStepErrorInTestSystem

> Category: `Test` | Type: `function`

## Syntax

```c
TestStep (dword LevelOfDetail, char Identifier[], char Description[], ...); // form 1
```

## Description

With these functions, test steps can be reported within a test case.

TestStep reports a test step without influence on the result.

TestStepPass reports a test step that was executed as expected. This is displayed accordingly in the test report.

TestStepFail describes a test step that causes an error. Also this is displayed accordingly in the test report. The verdict of the test case is hereby set automatically to fail.

TestStepWarning describes a test case that was executed without errors but whose result could contribute to a problem later on. This is represented appropriately in the test report.

TestStepInconclusive describes a test step which can not clearly marked as passed or failed . Also this is displayed accordingly in the test report. The verdict of the test case is hereby set automatically to inconclusive.

TestStepErrorInTestSystem describes a test step that causes an error in test system. Also this is displayed accordingly in the test report. The verdict of the test case is hereby set automatically to error in test system.

## Return Values

—

## Example

```c
TestStepPass("10.2", "Output voltage ok (Uout =  %d  volts)", voltage);
```

## Availability

| Since Version |
|---|
