# Iso11783OPSelectInput

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSelectInput( dword ecuHandle, dword objectID, dword select );
```

## Description

The function selects an input object. A Select Input command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPSelectInput( handle, 1200, 1 );
```

## Availability

| Since Version |
|---|
