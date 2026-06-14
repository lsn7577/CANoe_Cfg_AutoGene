# linResetManualChecksum

> Category: `LIN` | Type: `function`

## Syntax

```c
void linResetManualChecksum(linFrame linFrame)
```

## Description

Sets the correct checksum of a LIN frame, whose checksum has been changed by using linSetManualChecksum() function. The checksum is calculated using the frame data.

## Return Values

—

## Example

Reset checksum error caused by previously called linSetManualChecksum()

```c
...
linFrame MotorControl frmMotorControl;
linResetManualChecksum(frmMotorControl);
output(frmMotorControl); // it is important to call output() to make the changes active
```

## Availability

| Since Version |
|---|
