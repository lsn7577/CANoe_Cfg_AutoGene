# coTfsSetReportBehaviour

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetReportBehaviour( dword reportSetting );
```

## Description

With this function, the report behavior of the node layer can be set. In contrast to the function coTfsSetFailControl outputs were not interchanged but enabled/disabled selective.

The parameter reportSetting is a bit field and sets the behavior of the node layer. Per default all outputs are enabled (reportSettings=0x3FFFDFFF)

## Parameters

| Name | Description |
|---|---|
| Note If the output is disabled for test step pass/fail (bit 2 and bit 3), the verdict of the test function is not set by the CANopen® test module. It shall be set by the user test. |  |

## Return Values

Error code

## Example

```c
[globals section]
const kTestStepInit    = 0x00000001;
const kTestStep      = 0x00000002;
const kTestStepPass    = 0x00000004;
const kTestStepFail    = 0x00000008;
const kTestStepWarning   = 0x00000010;
const kTestStepResume   = 0x00000020;
const kTestStepInfo    = 0x00000040;
const kTestStepNone    = 0x00000000;
const kTestStepDefault = 0x3FFFDFFF;
const kTestStepAll = 0x3FFFDFFF;

[test case]
coTfsSetReportBehaviour( kTestStepAll );
```
