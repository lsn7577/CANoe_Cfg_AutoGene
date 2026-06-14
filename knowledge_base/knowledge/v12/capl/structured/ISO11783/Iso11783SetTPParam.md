# Iso11783SetTPParam

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783SetTPParam( dword ecuHandle, dword what, dword value );
```

## Description

Changing transport protocol settings.

## Return Values

0 on success or error code

## Example

```c
Iso11783SetTPParam(ecuHdl, 
 1, 32*1024 );
```

## Availability

| Since Version |
|---|
