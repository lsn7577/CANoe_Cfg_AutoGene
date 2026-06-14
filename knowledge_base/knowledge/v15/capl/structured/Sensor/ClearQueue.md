# ClearQueue

> Category: `Sensor` | Type: `method`

## Syntax

```c
SensorErrorCode SysVarNamespace.ClearQueue();
```

## Description

Clears the send queue of the given sensor system variable.

## Return Values

This method returns a SensorErrorCode.

## Example

```c
// Clears the send queue of a simulated PSI5 sensor channel
sysvar::SENSOR::PSI5::SensorChannel.ClearQueue();

// Clears the send queue of a simulated SENT sensor channel
sysvar::SENSOR::SENT::SensorChannel.ClearQueue();

// Clears queued read frames in case of I2C slave simulation or clears
// queued write / combined frames in case of I2C master simulation
sysvar::SENSOR::I2C::ExampleChannel::Slave1.ClearQueue();

// Clears MOSI send queue in case of SPI master simulation or MISO
// send queue in case of SPI slave simulation
sysvar::SENSOR::SPI::ExampleChannel::Slave1.ClearQueue();

// Clears send queue of UART channel
sysvar::SENSOR::UART::UARTChannel.ClearQueue();

// Clears send queue of LVDS channel
sysvar::SENSOR::LVDS::LVDSChannel.ClearQueue();

// Clears send queue of RS-485 channel
sysvar::SENSOR::RS485::RS485Channel.ClearQueue();
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
