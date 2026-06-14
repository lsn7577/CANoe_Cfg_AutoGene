# Iso11783IL_OPChangeFontAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeFontAttribute( dword objectID, dword color, dword size, dword type, dword style ); // form 1
```

## Description

The function changes the properties of a font attribute object. A Change Font Attribute command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeFontAttribute( 1100, 10, 3, 0, 0x01 );
```

## Availability

| Since Version |
|---|
