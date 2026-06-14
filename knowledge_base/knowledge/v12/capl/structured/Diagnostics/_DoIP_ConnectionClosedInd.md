# _DoIP_ConnectionClosedInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_ConnectionClosedInd( long reason);
```

## Description

The TCP connection to the peer has been closed, i.e. another exchange of diagnostic messages will require a connection setup. This callback is also called in a vehicle simulation.

## Return Values

—

## Example

```c
void _DoIP_ConnectionClosedInd( long reason)
{
  write( "ConnectionClosedInd( %d)", reason);
}
```

## Availability

| Since Version |
|---|
