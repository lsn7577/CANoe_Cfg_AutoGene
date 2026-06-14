# sensorClearQueue

> Category: `Sensor` | Type: `function`

## Syntax

```c
SensorErrorCode sensorClearQueue (char[] sysVarNamespace);
```

## Description

Clears the send queue of the given sensor system variable.

## Parameters

| Name | Description |
|---|---|
| sysVarNamespace | The namespace of the channel or sensor whose send queue should be cleared. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
// Clears the send queue of a simulated PSI5 sensor channel
sensorClearQueue("SENSOR::PSI5::SensorChannel");

// Clears the send queue of a simulated SENT sensor channel
sensorClearQueue("SENSOR::SENT::SensorChannel");

// Clears queued read frames in case of I2C slave simulation or clears
// queued write / combined frames in case of I2C master simulation
sensorClearQueue("SENSOR::I2C::ExampleChannel::Slave1");

// Clears MOSI send queue in case of SPI master simulation or MISO
// send queue in case of SPI slave simulation
sensorClearQueue("SENSOR::SPI::ExampleChannel::Slave1");

// Clears send queue of UART channel
sensorClearQueue("SENSOR::UART::UARTChannel");

// Clears send queue of LVDS channel
sensorClearQueue("SENSOR::LVDS::LVDSChannel");

// Clears send queue of RS-485 channel
sensorClearQueue("SENSOR::RS485::RS485Channel");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
