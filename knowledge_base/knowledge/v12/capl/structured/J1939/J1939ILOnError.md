# J1939ILOnError

> Category: `J1939` | Type: `function`

## Syntax

```c
void J1939ILOnError( long errorCode, long param )
```

## Description

This callback function is called from the J1939 IL if an error occurred.

## Return Values

—

## Example

```c
void J1939ILOnError( LONG errorCode, LONG param )
{
  write( "Error %d, parameter %d", errorCode, param );
}
```

## Availability

| Since Version |
|---|
