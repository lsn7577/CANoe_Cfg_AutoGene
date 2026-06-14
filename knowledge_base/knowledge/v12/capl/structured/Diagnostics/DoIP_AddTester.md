# DoIP_AddTester

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_AddTester( dword address);
```

## Description

Adds a valid DoIP tester address to the DoIP layer.

## Return Values

—

## Example

```c
dword address;
address = DiagGetCommParameter( “DoIP.TESTER_LogicalAddress")
DoIP_AddTester(address);
```

## Availability

| Since Version |
|---|
