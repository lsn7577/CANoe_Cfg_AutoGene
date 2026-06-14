# Iso11783OPOnValueChange

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnValueChange( dword ecuHandle, dword objectID );
```

## Description

The function is called by the node layer, if the value of an object is changed (with the command Change String Value or Change Numeric Value). The functions Iso11783OPGetStringValue and Iso11783OPGetNumericValue can be used to get the new value of the object.

## Return Values

—

## Example

```c
void Iso11783OPOnValueChange( dword handle, dword objectID )
{
}
```

## Availability

| Since Version |
|---|
