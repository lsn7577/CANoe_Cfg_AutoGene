# AREthGetLength

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetLength ( dword messageHandle );
```

## Description

This function returns the length in bytes that is in the SOME/IP message header.

## Return Values

Length of the SOME/IP message (without Message ID and length field)
In the Event of an error, the function returns the value 0. The AREthGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Availability

| Since Version |
|---|
