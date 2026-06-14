# Iso11783IL_TIMOnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_TIMOnError(long errorCode, dword addParam)
```

## Description

This callback function is called from the ISO11783 IL if an error occurred while TIM nodes are simulated.

## Return Values

0: Property has been set successfully

## Example

```c
void Iso11783IL_TIMOnError( long errorCode, dword addParam )
{
  char buffer[256];
  Iso11783IL_GetLastErrorText ( elCount(buffer), buffer);
  write( "Iso11783IL_TIMOnError: Error %i (%f): %s", errorCode,timeNowFloat()/100000.0, buffer );
}
```

## Availability

| Since Version |
|---|
