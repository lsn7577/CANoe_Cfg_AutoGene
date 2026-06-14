# linSetManualChecksum

> Category: `LIN` | Type: `function`

## Syntax

```c
void linSetManualChecksum(linFrame linFrame, byte csValue)
```

## Description

Sets a checksum (that is usually not a correct one) for a LIN frame.Text

## Return Values

—

## Example

```c
...
linFrame MotorControl frmMotorControl;
linSetManualChecksum(frmMotorControl, 0x1A);
output(frmMotorControl); // it is important to call output() to make the changes active
```

## Availability

| Since Version |
|---|
