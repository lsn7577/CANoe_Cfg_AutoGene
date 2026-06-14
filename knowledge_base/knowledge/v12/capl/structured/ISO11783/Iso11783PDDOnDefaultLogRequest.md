# Iso11783PDDOnDefaultLogRequest

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783PDDOnDefaultLogRequest( dword ecuHandle );
```

## Description

This function can be implemented in the CAPL program. The function is called up by the node layer if default logging is requested by the Task Controller. Default logging can then be started with the CAPL function Iso11783PDDSetLogTrigger.

## Return Values

—

## Example

```c
void Iso11783PDDOnDefaultLogRequest( dword ecuHandle )
{
  Iso11783PDDSetLogTrigger ( ecuHandle, 4, 0x0100, 0, 1000 );
  Iso11783PDDSetLogTrigger ( ecuHandle, 4, 0x0101, 0, 1000 );
}
```

## Availability

| Since Version |
|---|
