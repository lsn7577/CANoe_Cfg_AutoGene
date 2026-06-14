# ChkQuery_EventSignalValue

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventSignalValue (dword checkId, double pValue[]); // form 1
long ChkQuery_EventSignalValue (dword checkId, int64& value); // form 2
```

## Description

This function enables access to the signal value which was last reported by a check as invalid.

The signature of the function with the same name without the pValue parameter enables access only to positive signal values.

This function enables access to signal values in any directory.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Example

```c
CallbackOnSignalXyzViolation(dword aCheckId)
{
   double lBadValue[1]; // use an array to allow "call-by-reference"; length: 1 element
   ChkQuery_EventSignalValue(aCheckId, lBadValue);
   write("Last bad signal value=%g", lBadValue[0]);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 7.0 SP5: method 8.5 SP3: form 2 | 13.0 | — | 14 | 1.0 2.0 SP2: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
