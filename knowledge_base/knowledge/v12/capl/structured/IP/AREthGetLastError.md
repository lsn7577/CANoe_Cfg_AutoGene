# AREthGetLastError

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthGetLastError();
```

## Description

This function can be used to check whether the last called function of AUTOSAR Eth IL has been successfully executed. The call of this function does not reset the saved error.

In the Event of an error, a detailed error description can be read out using the AREthGetLastErrorText function.

## Return Values

0: The last called function was successfully executed

## Example

```c
long retVal;

// resume sending messages
AREthILControlResume();

// check if last function was executed correct
if((retVal = AREthGetLastError()) != 0)
{
  write("AUTOSAR Eth IL error occured: Error code: %d", retVal);
} // if
```

## Availability

| Since Version |
|---|
