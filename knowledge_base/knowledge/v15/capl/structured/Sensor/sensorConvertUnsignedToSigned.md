# sensorConvertUnsignedToSigned

> Category: `Sensor` | Type: `function`

## Syntax

```c
dword sensorConvertUnsignedToSigned(dword inputSignalValue, long& outputSignalValue, dword bitCount);
```

## Description

Converts the given n bit input value from unsigned to signed using two's complement.

## Parameters

| Name | Description |
|---|---|
| inputSignalValue | The unsigned input value. |
| outputSignalValue | The signed output value. |
| bitCount | The length of the input/output signal in bits. |

## Return Values

This function returns a SensorErrorCode.

## Example

```c
  dword inputValue = 13;
  dword outputValue;

  // Convert the 4 bit unsigned input value to a signed value
  sensorConvertUnsignedToSigned(inputValue, outputValue, 4);

  // outputValue is now -3.
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | Sensor | — | — | — | Sensor |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
