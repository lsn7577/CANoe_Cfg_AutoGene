# xlAcquireLED

> Category: `Other` | Type: `function`

## Syntax

```c
dword xlAcquireLED(dword ledBitMask);
```

## Description

Acquires the specified LEDs of a hardware device in order to set their operation mode with xlSetLED afterwards.

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

## Example

At measurement start three LEDs are acquired, two LEDs are set to condition "orange glowing", and one is set to the condition "orange flashing". At measurement stop the LEDs should be released.

```c
/*@@var:*/
variables
{
   // constants for LED access
   const dword kLedMaskC1         = 0x008;
   const dword kLedMaskC2         = 0x010;
   const dword kLedMaskC3         = 0x020;
   // constants for LED operation modes
   const dword kLedOrangeOn       = 0x00000020;
   const dword kLedOrangeBlinking = 0x00000040;

   dword status;
}
/*@@end*/

/*@@startStart:Start:*/
on start
{
   status = xlAcquireLED(kLedMaskC1 | kLedMaskC2 | kLedMaskC3);
   if( 0 == status)
   {
      xlSetLed(kLedMaskC1 | kLedMaskC2, kLedOrangeOn);
      xlSetLed(kLedMaskC3, kLedOrangeBlinking);
   }
}
/*@@end*/

/*@@stop:StopMeasurement:*/
on stopMeasurement
{
   if( 0 == status)
   {
      xlReleaseLED(kLedMaskC1 | kLedMaskC2 | kLedMaskC3);
   }
}
/*@@end*/
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 SP6 | 7.2 SP6 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
