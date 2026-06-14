# linSetChannelMasterMode

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetChannelMasterMode(long masterMode);
```

## Description

By calling this function, the channel specified by the current bus context can be switched to master or slave mode. See SetBusContext for how to change the current bus context. The impacts of switching a LIN hardware channel to master or slave are described in Master Mode of the LIN Hardware. In simulated mode, the only effect is that sending a LIN header in slave mode (by calling linTransmitHeader or output(linFrame) with linFrame.RTR = 1) will have no effect.

This function can be called at any time. If a LIN scheduler is defined by using a LDF, calling this function will deactivate the scheduler when changing to slave mode. When changing back to master mode, the scheduler’s running state will be restored to its state before changing to slave mode.

A channel configured to slave mode by the settings of the network hardware dialog still can contain a master node defined in an attached LDF file. The scheduler of that channel will be automatically activated when the channel is switched to master mode.

## Parameters

| Name | Description |
|---|---|
| masterMode | This parameter specifies whether the Master mode will be enabled or disabled on the LIN channel. 0: Disable 1: Enable |

## Return Values

returns 1 if changing the channel master mode succeeded, 0 otherwise.

## Example

```c
linSetChannelMasterMode(1); // manually activate the Master mode on LIN hardware
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | 13.0 | — | — |
| Restricted To | — | LIN de | LIN | LIN | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
