# coOnError

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnError( dword errorCode, dword errorClass, dword nodeId, dword index, dword subIndex, dword param );
```

## Description

This function is called if an error occurs.

## Return Values

—

## Example

```c
void coOnError( dword errorCode, dword errorClass, dword nodeId, dword index, dword subIndex, dword param){
  write( "Error occurred, code = 0x%X, class = %d", errorCode, errorClass );
}
```

## Availability

| Up to Version |
|---|
