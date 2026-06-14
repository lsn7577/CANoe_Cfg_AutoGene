# xcpSendRaw

> Category: `XCP` | Type: `function`

## Syntax

```c
void xcpSendRaw(char ecuQualifier[], byte data[], long dataSize, byte expectResponse);
```

## Description

Sends any data as control command to an XCP/CCP device. The first data byte defines the control command code.

The callback is called with the response to a raw XCP command sent by xcpSendRaw.

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

| Since Version |
|---|
