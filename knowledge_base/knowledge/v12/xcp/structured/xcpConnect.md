# xcpConnect

> Category: `XCP` | Type: `function`

## Syntax

```c
long xcpConnect (char ecuQualifier[]);
```

## Description

Establishes a connection to the XCP/CCP device and starts the configured DAQ measurement.

If the connection is successfully depends on the response of the device.

Use xcpIsConnected to be aware of the connection.

After establishing the connection and before start of the DAQ measurement the callback function OnXcpConnect is called.

## Return Values

0: OK

## Example

```c
testcase TC_ConnectToECU ()
{
  xcpConnect("ECU");
....
}

//Callback function:
void OnXcpConnect (char ecuQualifier[])
{
  //Set calibration page to RAM
  xcpSetCalPage(ecuQualifier, 0x83, 0, 0);
}
```

## Availability

| Since Version |
|---|
