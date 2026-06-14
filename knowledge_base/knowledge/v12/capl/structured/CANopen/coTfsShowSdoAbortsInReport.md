# coTfsShowSdoAbortsInReport

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsShowSdoAbortsInReport( dword enable );
```

## Description

Allows the report of SDO aborts in the test protocol. If the function is activated in the test module (default), each recognized SDO abort code is added to the test report.

## Return Values

Error code

## Example

```c
coTfsShowSdoAbortsInReport(1); // enable SDO abort reports in test report
```
