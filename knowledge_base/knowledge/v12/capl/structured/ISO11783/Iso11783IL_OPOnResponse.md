# Iso11783IL_OPOnResponse

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_OPOnResponse( pg VTtoECU response );
```

## Description

The function is called by the node layer, if a response from the Virtual Terminal is received. If a response is not received, the callback function Iso11783IL_OPOnError is called.

## Return Values

—

## Example

```c
void Iso11783IL_OPOnResponse( pg VTtoECU response )
{
}
```

## Availability

| Since Version |
|---|
