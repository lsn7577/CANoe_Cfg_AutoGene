# CANstressCreateServer(DeviceAlias)

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressCreateServer (char[] deviceAlias);
```

## Description

Starts the CANstress software and establishes a connection to this COM server via the COM interface. The COM server generated only establishes a connection to the CANstress device defined in deviceAlias. Connected CANstress devices are mapped to an alias using the canstress.INI file. You will find this file in the CANstress software’s installation directory. If the call is successful, the device defined in deviceAlias will be set as the current device.

## Return Values

> 0: If successful.If the attempt to establish a connection to a COM server is successful, a handle required for the CANstressSetDevice function will be returned for the device. This handle will be a value greater than 0.

## Availability

| Since Version |
|---|
