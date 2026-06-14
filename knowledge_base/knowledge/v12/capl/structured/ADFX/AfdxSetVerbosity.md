# AfdxSetVerbosity

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxSetVerbosity( long verbosity );
```

## Description

This function sets the verbosity level of the AFDX IL.

The default setting is that only error messages are written to the Write Window of CANoe.

## Return Values

0 or error code

## Example

```c
// do not print AFDX IL messages to Write Window
AfdxSetVerbosity( 0 );
```

## Availability

| Since Version |
|---|
