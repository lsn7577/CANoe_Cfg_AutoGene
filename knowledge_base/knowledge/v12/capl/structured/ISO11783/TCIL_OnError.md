# TCIL_OnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void TCIL_OnError( long errorCode, long param );
```

## Description

This callback function is called from the TC IL if an error occurred.

## Return Values

—

## Example

```c
void TCIL_OnError( long errorCode, long param )
{
  write( "Error %d, parameter %d", errorCode, param );
}
```

## Availability

| Since Version |
|---|
