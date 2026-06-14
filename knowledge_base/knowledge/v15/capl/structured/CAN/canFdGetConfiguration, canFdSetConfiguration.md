# canFdGetConfiguration, canFdSetConfiguration

> Category: `CAN` | Type: `function`

## Syntax

```c
long canFdSetConfiguration(long channel, canSettings abrSettings, canSettings dbrSettings);
long canFdGetConfiguration(long channel, canSettings abrSettings, canSettings dbrSettings);
```

## Description

The CAN controller parameters for arbitration and data phase can be set or read

canFdSetConfiguration performs an automatic reset of the CAN controller.

## Parameters

| Name | Description |
|---|---|
| Channel | The CAN channel. |
| Bit Position | Value, Description |
| 0, 1 | 0: unknown transceiver 1: Low speed 2: Single wire 3: High speed |
| 8 | 0x100: The channel is configured for CAN FD |
| All others | Reserved |
| Bit Position | Value, Description |
| 0 | 0: normal mode 1: silent mode (acknowledge not created) |
| All others | Reserved, and must be 0. |

## Example

```c
int ret;
int channel = 1;
CANsettings abrSettings;

CANsettings dbrSettings;

abrSettings.baudrate = 1000000;
abrSettings.tseg1=5;
abrSettings.tseg2=2;
abrSettings.sjw=2;
abrSettings.sam=1;
abrSettings.flags = 0;

dbrSettings.baudrate = 4000000;
dbrSettings.tseg1=6;
dbrSettings.tseg2=3;
dbrSettings.sjw=2;
dbrSettings.sam=1;
dbrSettings.flags = 0;

write("Set 1 MB");
ret = canFdSetConfiguration(channel, abrSettings, dbrSettings);

if (ret)
{
write("Arbitration settings: baud= %f, tseg1 = %d, tseg2= %d, sjw = %d, sam = %d, flags = 0x%x",abrSettings.baudrate, abrSettings.tseg1, abrSettings.tseg2, abrSettings.sjw, abrSettings.sam, abrSettings.flags);
write("Data settings: baud= %f, tseg1 = %d, tseg2= %d, sjw = %d, sam = %d, flags = 0x%x",dbrSettings.baudrate, dbrSettings.tseg1, dbrSettings.tseg2, dbrSettings.sjw, dbrSettings.sam, dbrSettings.flags);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 SP4 | 8.0 SP4 | 13.0 | — | — | 1.0 |
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
| Since Version | 8.2 | 8.2 | 13.0 | — | — | 1.1 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
