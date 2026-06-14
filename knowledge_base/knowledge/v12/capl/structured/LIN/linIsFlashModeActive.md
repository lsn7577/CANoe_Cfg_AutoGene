# linIsFlashModeActive

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linIsFlashModeActive()
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

| Since Version |
|---|
