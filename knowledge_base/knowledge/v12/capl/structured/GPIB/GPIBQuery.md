# GPIBQuery

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBQuery (long deviceDescriptor, char cmdStr[]);
```

## Description

Query to the device.

The cmdStr is put to a queue, and then the function returns immediately. When the cmdStr has been sent to the device, and a response has been received, the user-supplied function GPIBResponse is called.

## Return Values

Status

## Example

```c
Query of the voltage: GPIBQuery(myDev, "V?")
```

## Availability

| Since Version |
|---|
