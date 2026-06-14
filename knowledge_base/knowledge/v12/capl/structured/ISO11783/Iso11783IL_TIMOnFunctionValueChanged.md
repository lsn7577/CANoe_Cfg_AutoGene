# Iso11783IL_TIMOnFunctionValueChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_TIMOnFunctionValueChanged(dword functionID, dword newRawValue)
```

## Description

This callback function is called if the value of a function has been changed due to a function request message. It is not called when a function request command failed (e.g. because function is not assigned or value is out of range).

## Parameters

| Name | Description |
|---|---|
| Function ID | Description |
| 1-32 (1h-20h) | Auxiliary Value 1 – 32 |
| 64 (40h) | Front PTO |
| 65 (41h) | Rear PTO |
| 66 (42h) | Front hitch |
| 67 (43h) | Rear hitch |
| 68 (44h) | Vehicle speed |
| 70 (46h) | External guidance |

## Return Values

—

## Availability

| Since Version |
|---|
