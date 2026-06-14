# AvbGetLastError

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbGetLastError( );
```

## Description

This function can be used to check whether the last called function of AVB IL has been successfully executed. The call of this function does not reset the saved error.

In the Event of an error, a detailed error description can be read out using the AvbGetLastErrorText function.

## Return Values

0: The last called function was successfully executed.

## Example

```c
dword retVal;
dword listenerHandle;

// open a listener
listenerHandle = AvbOpenListener();

// check if last function was successfully executed
if ((retVal = AvbGetLastError()) != 0)
{
  write("AVB IL error occured: Error code: %d", retVal);
}
```

## Availability

| Since Version |
|---|
