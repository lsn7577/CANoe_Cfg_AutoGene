# coTfsShowEmergenciesInReport

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsShowEmergenciesInReport( dword enable );
```

## Description

Allows the report of emergency code in the test protocol. If the function is activated in the test module (default), each recognized emergency code is added to the test report.

## Return Values

Error code

## Example

```c
coTfsShowEmergenciesInReport(1); // enable writing emergency codes to test report
```
