# GPIBQueryEx

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBQueryEx (long deviceDescriptor, char cmdStr[], long size);
```

## Description

Query to the device.

The cmdStr is put to a queue, and then the function returns immediately. When the cmdStr has been sent to the device, and a response has been received, the user-supplied function GPIBResponse is called.

## Return Values

Status

## Example

```c
Query after wave form: GPIBQuery(myDev, "WAVF?", 1024)
```

## Availability

| Since Version |
|---|
