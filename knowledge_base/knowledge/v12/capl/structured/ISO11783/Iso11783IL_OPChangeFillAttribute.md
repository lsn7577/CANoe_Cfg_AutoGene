# Iso11783IL_OPChangeFillAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeFillAttribute( dword objectID, dword color, dword type, dword patternID );
```

## Description

The function changes the properties of a fill attribute object. A Change Fill Attribute command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeFillAttribute( 1100, 12, 2, 0xFFFF );
```

## Availability

| Since Version |
|---|
