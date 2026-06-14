# TestGroupBegin

> Category: `Test` | Type: `function`

## Syntax

```c
TestGroupBegin (char title[], char description[]);
```

## Description

A test group is opened with this function. It may only be called in a test module, but not in a test case. All test cases and test groups that are executed before call of the corresponding function TestGroupEnd are part of this test group. If a test group is not closed with TestGroupEnd, then at the end of the test module, a warning is written in the Write Window and the test group is closed automatically.

To obtain line breaks (in form of <br /> tags) in the test report, "\n" may be inserted at any place.

## Return Values

—

## Availability

| Since Version |
|---|
