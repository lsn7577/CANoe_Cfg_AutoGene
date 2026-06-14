# linIsFlashModeActive

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linIsFlashModeActive();
```

## Description

This function reports the flash mode state on high-speed capable transceivers.

## Return Values

Returns 1 if flash mode is active, otherwise 0.

## Example

```c
// test case for disturbing parts of a bit
// note, that test cases can only be used in the context of test module nodes

testcase tcDisturbPartialBit()
{
   dword flashModeActive;

   flashModeActive = 0;

   do
   {
      if (!linActivateFlashMode(1)) // request activation of flash mode
      {
         break; // if the request has been denied, either the cab/piggy is incapable of
                // flash mode or the scheduler is still running
      }
      testWaitForTimeout(10); // give the hardware time to activate the flash mode
      flashModeActive = linIsFlashModeActive(); // check if flash mode has been
                                                // activated successfully
   } while (!flashModeActive);

   if (!flashModeActive)
   {
      testStepFail(“tcDisturbPartialBit”, “Flash mode could not be activated because of active scheduler or because the cab/piggy does not support flash mode.”);
      return;
   }

   linInvertRespBitEx(0, 0, 8, 4, 8, 0); // invert the middle part of the stop bit of the
                                         // first byte of the response to id 0

...
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 SP2 | — | — | — | 2.2 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
