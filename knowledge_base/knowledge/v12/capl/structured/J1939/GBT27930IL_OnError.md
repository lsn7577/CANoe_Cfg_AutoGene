# GBT27930IL_OnError

> Category: `J1939` | Type: `function`

## Syntax

```c
void GBT27930IL_OnError( long errorCode, long param )
```

## Description

This callback function is called from the GBT27930 IL if an error occurred.

## Return Values

—

## Example

```c
void GBT27930IL_OnError( LONG errorCode, LONG param )
{
  write( "Error %d, parameter %d", errorCode, param );
}
```

## Availability

| Since Version |
|---|
