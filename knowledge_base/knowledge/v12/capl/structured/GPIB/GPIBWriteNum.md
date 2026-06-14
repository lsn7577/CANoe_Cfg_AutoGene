# GPIBWriteNum

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBWriteNum (long deviceDescriptor, char cmdStr[], double value);
```

## Description

Writes cmdStr + numeric value to the device.

The function returns immediately and does not wait for the end of the command transmission.

## Return Values

Status

## Example

```c
Setting of a voltage of 1.23 V: GPIBWriteStr(myDev, "V", 1.23)
```

## Availability

| Since Version |
|---|
