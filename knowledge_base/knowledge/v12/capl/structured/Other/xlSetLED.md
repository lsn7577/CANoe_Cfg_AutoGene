# xlSetLED

> Category: `Other` | Type: `function`

## Syntax

```c
dword xlSetLED(dword ledBitMask, dword ledMode);
```

## Description

Sets the LEDs specified by ledBitMask to the operation mode specified by ledMode. A successful call of xlAcquireLED is necessary before the operation mode of an LED can be set with this function.

This function is only supported on VN8900 devices.

Note that for every successful call of xlAcquireLED on a specific LED, you have to call xlReleaseLED to release this LED again.

## Parameters

| Name | Description |
|---|---|
| LED | Numeric Value |
| Module (M) | 0x001 |
| CAN Channel 1 | 0x008 |
| CAN Channel 2 | 0x010 |
| CAN Channel 3 | 0x020 |
| CAN Channel 4 | 0x040 |
| FlexRay Channel 1 A | 0x080 |
| FlexRay Channel 1 B | 0x100 |
| Keypad S1 | 0x200 |
| Keypad S2 | 0x400 |

## Return Values

0: no error, function succeeded.

## Availability

| Since Version |
|---|
