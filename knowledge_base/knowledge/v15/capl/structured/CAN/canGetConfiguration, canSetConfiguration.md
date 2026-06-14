# canGetConfiguration, canSetConfiguration

> Category: `CAN` | Type: `function`

## Syntax

```c
long canGetConfiguration(long channel, canSettings settings);
long canSetConfiguration(long channel, canSettings settings);
```

## Description

The CAN controller parameters can be set or read.

canSetConfiguration performs an automatic reset of the CAN controller.

## Parameters

| Name | Description |
|---|---|
| Channel | The CAN channel. |
| Bit Position | Value, Description |
| 0, 1 | 0: unknown transceiver 1: Low speed 2: Single wire 3: High speed |
| 8 | 0x100: The channel is configured for CAN FD |
| All others | Reserved |
| Bit Position | Value, Description |
| 0 | 0: Normal mode 1: Silent mode (acknowledge not created) |
| All others | Reserved, and must be 0. |

## Example

```c
int ret;
int channel = 1;
canSettings settings;
settings.baudrate = 1000000;
settings.tseg1=5;
settings.tseg2=2;
settings.sjw=2;
settings.sam=1;
settings.flags = 0;

write("Set 1 MB");
ret = canSetConfiguration(channel, settings);

ret = canGetConfiguration(channel, settings);
if (ret)
{
   write("Settings: baud= %f, tseg1 = %d, tseg2= %d, sjw = %d, sam = %d, flags = 0x%x",
             settings.baudrate, settings.tseg1, settings.tseg2, settings.sjw, settings.sam, settings.flags);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
| Since Version | 8.0 | 8.0 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
