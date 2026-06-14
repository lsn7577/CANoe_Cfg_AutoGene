# J1939SetTPParam

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939SetTPParam( dword ecuHandle, dword what, dword value );
```

## Description

Changing transport protocol settings.

## Return Values

0 on success or error code

## Example

```c
J1939SetTPParam(ecuHdl, 
 1, 32*1024 );
```

## Availability

| Since Version |
|---|
