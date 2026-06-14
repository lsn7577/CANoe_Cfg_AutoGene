# VTIL_OnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void VTIL_OnError( long errorCode, long param );
```

## Description

This callback function is called from the VT IL if an error occurred.

## Return Values

—

## Example

```c
void VTIL_OnError( long errorCode, long param )
{
  write( "Error %d, parameter %d", errorCode, param );
}
```

## Availability

| Since Version |
|---|
