# SerialReceive

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long SysVarNamespace.SerialReceive( byte buffer[], dword size);
```

## Description

Starts receiving blocks of bytes from the serial port of the specified VT7001 channel. Received data is copied to the specified buffer. The data can only be accessed in the OnSerialReceive callback.

The used serial port has to be opened first.

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
