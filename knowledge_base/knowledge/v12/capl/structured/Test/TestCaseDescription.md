# TestCaseDescription

> Category: `Test` | Type: `function`

## Syntax

```c
TestCaseDescription (char description[]);
```

## Description

With this function, a description test for a test case can be written into the report. The function can be called several times in a row, the transmitted texts are then added to one another without additional separation. The function may only be called within a test case and relates then to the respective test case.

To obtain line breaks (in form of <br /> tags) in the test report, "\n" may be inserted at any place.

## Return Values

—

## Example

```c
// add description with line break to report
TestCaseDescription("In this test case\nthe occurrence of Error Frames is tested.");
```

## Availability

| Since Version |
|---|
