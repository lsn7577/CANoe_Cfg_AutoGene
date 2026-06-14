# canFlushTxQueue

> Category: `CAN` | Type: `function`

## Syntax

```c
long canFlushTxQueue(long channel);
```

## Description

Flushes the Tx queue for the defined channel.

## Parameters

| Name | Description |
|---|---|
| Channel | The CAN channel. |

## Example

```c
on key 'f'
{
  int result;
  //flush Tx queue for CAN channel 1

  result = canFlushTxQueue(1);
  if(result == 1)
    write("Tx queue flushed ");
  else
    write("Tx queue flush failed Result =%d ", result);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP2 | 10.0 SP2 | 13.0 | — | — | 2.2 SP2 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
