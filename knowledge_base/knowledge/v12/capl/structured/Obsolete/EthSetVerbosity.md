# EthSetVerbosity

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthSetVerbosity( long verbosity);
```

## Description

This function set the verbosity level of the Ethernet IL.

The default setting is that only error messages are written to the Write Window of CANoe.

## Return Values

0 or error code

## Example

```c
// do not print Ethernet IL messages to Write Window
EthSetVerbosity( 0 );
```

## Availability

| Up to Version |
|---|
