# Iso11783IL_PDDOnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_PDDOnError( long errorCode, dword param );
```

## Description

This function can be implemented in the CAPL program. The function is called up by the interaction layer when an error occurs.

## Return Values

—

## Example

```c
void Iso11783IL_PDDOnError( LONG errorCode, LONG addParam )
{
  char buffer[256];
  Iso11783IL_PDDGetLastErrorText ( elCount(buffer), buffer);
  write( "ERROR: %s", buffer );
}
```

## Availability

| Since Version |
|---|
