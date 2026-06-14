# linChangeDlc

> Category: `LIN` | Type: `function`

## Syntax

```c
long linChangeDlc(long frameID, long dlc)
```

## Description

Changes the Data Length Code (i.e. length in bytes) of a LIN frame during the measurement.

Per default the DLC of LIN frames is initialized according to the LIN Description File (LDF). This function is therefore only needed if you are simulating LIN nodes without using a LDF and need to change the DLC of a LIN frame during the measurement.

To initialize the DLC of a LIN frame the function linSetDlc should be used in the event procedure on preStart.

## Return Values

If successful a value unequal to zero.

## Example

Change DLC of a frame from database

```c
...
linFrame MotorControl frameMotorControl;
linChangeDLC(frameMotorControl.id, frameMotorControl.dlc-1);
// now on transmitting the above frame a checksum error will come
```

## Availability

| Since Version |
|---|
