# FSIL_OnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void FSIL_OnError( long errorCode, long param );
```

## Description

Is called if an error has occurred.

## Return Values

—

## Example

```c
void FSIL_OnError( long errorCode, long param )
{
  write( "Error %d, parameter %d", errorCode, param );
}
```

## Availability

| Since Version |
|---|
