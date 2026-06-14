# AREthGetValueFloat

> Category: `IP` | Type: `function`

## Syntax

```c
float AREthGetValueFloat( dword objectHandle, char valuePath[] );
```

## Description

This function can be used to read out a raw value from the object specified in the objectHandle parameter. The value is accessed in this case via symbolic access paths.

## Return Values

Raw value
In the Event of an error, the function returns the value 0. The AREthGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Availability

| Since Version |
|---|
