# Iso11783IL_OPSelectInput

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSelectInput( dword objectID, dword select ); // form 1
```

## Description

The function selects an input object. A Select Input command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPSelectInput( 1200, 1 );
```

## Availability

| Since Version |
|---|
