# Iso11783OPOnPointingEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnPointingEvent( dword ecuHandle, long x, long y, dword state );
```

## Description

The function is called by the node layer, if the user clicks into the data mask.

## Return Values

—

## Example

```c
void Iso11783OPOnPointingEvent( dword handle, LONG x, LONG y, dword touchState )
{
}
```

## Availability

| Since Version |
|---|
