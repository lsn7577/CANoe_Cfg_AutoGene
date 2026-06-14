# GPIBWriteStr

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBWriteStr (long deviceDescriptor, char cmdStr[]);
```

## Description

Writes cmdStr to the device.

The function returns immediately and does not wait for the end of the command transmission.

## Return Values

Status

## Example

```c
Setting of a voltage of 1.23 V: GPIBWriteStr(myDev, "V 1.23")
```

## Availability

| Since Version |
|---|
