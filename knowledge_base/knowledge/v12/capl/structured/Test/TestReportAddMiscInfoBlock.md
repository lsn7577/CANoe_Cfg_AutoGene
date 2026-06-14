# TestReportAddMiscInfoBlock

> Category: `Test` | Type: `function`

## Syntax

```c
TestReportAddMiscInfoBlock (char title[]);
```

## Description

The function generates a new information block for additional information pairs in the report. With the function TestReportAddMiscInfo information pairs can be taken up into this block. This is possible until a new information block is opened with TestReportAddMiscInfoBlock, the current test case is ended (if the information block was opened within the test case) or a test case is called (if the information block was called in the test module).

## Return Values

—

## Availability

| Since Version |
|---|
