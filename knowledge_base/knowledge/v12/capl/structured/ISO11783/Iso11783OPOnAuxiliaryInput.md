# Iso11783OPOnAuxiliaryInput

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnAuxiliaryInput( dword ecuHandle, dword objectID, dword value1, dword value2 );
```

## Description

The function is called by the node layer, if an Auxiliary Input Status is received and a Auxiliary Function in the object pool is assigned.

## Return Values

—

## Example

```c
void Iso11783OPOnAuxiliaryInput(dword handle, dword objectID, dword value1, dword value2 
 )
{
}
```

## Availability

| Since Version |
|---|
