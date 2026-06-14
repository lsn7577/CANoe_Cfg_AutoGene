# Iso11783OPOnResponse

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnResponse( dword ecuHandle, pg VTtoECU response );
```

## Description

The function is called by the node layer, if a response from the Virtual Terminal is received. If a response is not received, the callback function Iso11783OPOnError is called.

## Return Values

—

## Example

```c
void Iso11783OPOnResponse( dword handle, pg VTtoECU response )
{
}
```

## Availability

| Since Version |
|---|
