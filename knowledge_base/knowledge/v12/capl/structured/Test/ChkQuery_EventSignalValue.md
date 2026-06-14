# ChkQuery_EventSignalValue

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventSignalValue (dword checkId, double pValue[]); // form 1
check.QueryEventSignalValue (double pValue[]); // form 1
```

## Description

This function enables access to the signal value which was last reported by a check as invalid.

The signature of the function with the same name without the pValue parameter enables access only to positive signal values.

This function enables access to signal values in any directory.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

<= 0: Refers the query error codes in this chapter

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

| Since Version |
|---|
