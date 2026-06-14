# Iso11783IL_OnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_OnError( long errorCode, long param );
```

## Description

This callback function is called from the ISO11783 IL if an error occurred.

## Return Values

—

## Example

```c
void Iso11783IL_OnError( LONG errorCode, LONG param )
{
  write( "Error %d, parameter %d", errorCode, param );
}
```

## Availability

| Since Version |
|---|
