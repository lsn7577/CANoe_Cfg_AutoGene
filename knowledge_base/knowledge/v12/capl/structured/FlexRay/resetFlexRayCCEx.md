# resetFlexRayCCEx

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long resetFlexRayCCEx (int channel, int wuChMask, int wuCount, int wuTxIdle, int wuTxLow, char[] cfg);
```

## Description

This function initializes the FlexRay Communication Controller (CC) and generates the specified wake-up pattern before reintegration in the cluster or the start-up.

## Return Values

—

## Example

The following program resets the FlexRay interface of the attached channel and sends a wake-up (if network is idle), when the <W> key is pressed.

```c
on key 'w'
{
   int wuChMask = 3;    // send wake-up on both channels
   int wuCount  = 4;    // send symbol 2 times (range 2-63)
   int wuTxIdle = 180;  // idle time of symbol in bit (range 0-255)
   int wuTxLow = 60;    // low time of symbol in bit (range 0-63)
   CHAR cfg[1];         // <cfg> -> not used yet
   resetFlexRayCCEx(%CHANNEL%,wuChMask,wuCount,wuTxIdle,wuTxLow,cfg);
   Write("FlexRay CC %d is reset and sending a wakeup.", %CHANNEL%);
}
```

## Availability

| Since Version |
|---|
