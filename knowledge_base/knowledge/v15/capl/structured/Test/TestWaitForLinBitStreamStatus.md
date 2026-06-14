# TestWaitForLinBitStreamStatus

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinBitStreamStatus(dword awaitedStatus, dword timeout); // form 1
long TestWaitForLinBitStreamStatus(dword channel, dword awaitedStatus, dword timeout); // form 2
```

## Description

Waits until the sending of a LIN bit stream is started or stopped. The function will resume immediately if the transmission already has the awaited status.

Should the event not occur before the expiration of the time timeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| awaitedStatus | 0: Sending of the bit stream is stopped. 1: Sending of the bit stream is started. |
| channel | The LIN channel number which will be queried. |
| timeout | Maximum time that should be waited [ms]. (Transmission of 0: no timeout controlling). |

## Example

```c
testcase tc_TestWaitForLinBitStreamStatus()
{
  long  result;

  // Wait for a maximum time of 100ms for the bit stream to start sending
  result = TestWaitForLinBitStreamStatus(1, 100);

  if(result != 1)
  {
    testStepFail("The sending of the bit stream didn't start within 100ms!");
    testCaseFail();
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | 13.0 | — | — | 2.2 |
| Restricted To | — | LIN Real bus mode | LIN Real bus mode | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
