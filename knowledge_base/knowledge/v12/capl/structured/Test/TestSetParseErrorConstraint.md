# TestSetParseErrorConstraint

> Category: `Test` | Type: `function`

## Syntax

```c
void TestSetParseErrorConstraint (long mode);
```

## Description

The function sets the behavior of the symbolic variants of TestWaitForMost... and TestJoinMost... functions on the occurrence of errors during the parsing of the message definitions.

Depending on whether the function is called within or outside of a test case, the setting either has an effect on only all subsequent TestWaitForMost... and TestJoinMost... function calls within the test case or generally on all subsequent calls. Therefore, the behavior specified within a test case loses its validity with the end of the test case and will be, if necessary, replaced by a previously externally-set behavior.

## Parameters

| Name | Description |
|---|---|
| 0 | The return value of the relevant function call indicates the problem that has occurred and a corresponding note is entered in the report. This is the pre-set default behavior. |
| 1 | The relevant test case is aborted and the verdict set to "fail". The aborting of the test case is noted with the error in the report. |
| 2 | Measurement will be stopped. The relevant test case is aborted and the verdict set to "fail". The aborting of the test case is noted with the error in the report. |

## Return Values

—

## Availability

| Since Version |
|---|
