# TestWaitForLinCSError

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForLinCSError(dword aTimeout);
long TestWaitForLinCSError(dword aFrameId, dword aTimeout);
```

## Description

Waits for a checksum error for the specified amount of time.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Timeout in milliseconds |
| aFrameId | Frame identifier |

## Example

```c
testcase tcTFS_linCSError ()
{
   linCSError linCSErrorData;
   if (testWaitForLinCSError(5000) == 1)
   {
      if (testGetWaitLinCSErrorData(linCSErrorData) == 0)
      {
         testStep("Evaluation", "LIN CS Error event occurred for FrameId=0x%X", linCSErrorData.ID);
      }
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
