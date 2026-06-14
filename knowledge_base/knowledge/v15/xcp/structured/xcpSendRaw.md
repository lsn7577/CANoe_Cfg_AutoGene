# xcpSendRaw

> Category: `XCP` | Type: `function`

## Syntax

```c
void OnXcpSendRaw(char ecuQualifier[], byte data[], long dataSize);
```

## Description

Sends any data as control command to an XCP/CCP device. The first data byte defines the control command code.

The callback is called with the response to a raw XCP command sent by xcpSendRaw.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Name of the device, configured within the CANoeXCP/CCP Window. |
| data | Byte array of the data to be sent. |
| dataSize | Length of the data to be sent. |
| expectResponse | 0: The XCP slave will not respond to this command 1: The XCP slave is expected to respond to this command and the callback will be called |

## Return Values

—

## Example

```c
//This example shows an upload of 4 bytes from address 0x21A1B4 of the XCP slave device "XCPsim" when the user presses the key 't'.
//Please note that this device is a PC application, hence the address is given in Intel format.

on key 't'
{
  byte data[8] = {0xF4, 4, 0, 0, 0xB4, 0xA1, 0x21, 0};
  xcpSendRaw("XcpSim", data, 8, 1);
}

OnXcpSendRaw(char ecuQualifier[], byte data[], long dataSize)
{
  char buffer[200];
  long i;
  buffer[0] = 0;
  for (i = 0; i < dataSize; i++)
  {
    snprintf(buffer, elcount(buffer), "%s 0x%2X", buffer, data[i]);
  }
  write("Raw response: %d bytes:%s", dataSize, buffer);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | XCP | XCP | — | — | XCP |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
