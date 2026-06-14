# SomeIpGetLastError

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpGetLastError();
```

## Description

This function can be used to check whether the last called function of SOME/IP IL has been successfully executed. The call of this function does not reset the saved error.

In the Event of an error, a detailed error description can be read out using the SomeIpGetLastErrorText function.

## Return Values

0: The last called function was successfully executed

## Example

```c
long retVal;

// resume sending messages
SomeIpILControlResume();

// check if last function was executed correct
if((retVal = SomeIpGetLastError()) != 0)
{
  write("SOME/IP IL error occured: Error code: %d", retVal);
} // if
```

## Availability

| Since Version |
|---|
