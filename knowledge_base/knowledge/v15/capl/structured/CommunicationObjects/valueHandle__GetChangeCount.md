# valueHandle::GetChangeCount

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
dword valueHandle::GetChangeCount()
```

## Description

Returns the change count of the value. The change count is reset to zero at start of measurement and with each call to valueHandle::ResetValueState. It is then increased each time the value changes (but not if it is updated with the same value).

For some values, the count is only initialized when the value is accessed the first time for performance reasons. This means that if you want to use it as a ‘global’ count over the whole measurement, you should call valueHandle::ResetValueState at the start of the measurement explicitly.

## Return Values

The current change count.

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.ResetValueState();
testWaitForTimeout(1000);
write("Changes during the last second: %d", MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.GetChangeCount());
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
