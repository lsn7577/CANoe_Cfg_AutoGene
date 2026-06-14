# C2xSetVerbosity

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetVerbosity( long verbosity );
```

## Description

This function sets the verbosity level of the Car2x IL.

The default setting is that only error messages are written to the Write Window of CANoe.

## Return Values

0 or error code.

## Example

```c
// do not print Car2x IL messages to Write Window
C2xSetVerbosity( 0 );
```

## Availability

| Since Version |
|---|
