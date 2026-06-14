# sensorConvertUnsignedToSigned

> Category: `Sensor` | Type: `function`

## Syntax

```c
dword sensorConvertUnsignedToSigned(dword inputSignalValue, long& outputSignalValue, dword bitCount);
```

## Description

Converts the given n bit input value from unsigned to signed using two's complement.

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

| Since Version |
|---|
