# AREthGetData

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetData( dword messageHandle, dword bufferLength, char buffer[] ); // form 1
dword AREthGetData( dword messageHandle, dword bufferLength, byte buffer[] ); // form 2
dword AREthGetData( dword messageHandle, dword bufferLength, struct buffer[] ); // form 3
```

## Description

This function can be used to query the raw data of a SOME/IP message.

## Parameters

| Name | Description |
|---|---|
| messageHandle | Handle of the received SOME/IP message (see OnAREthMessage) |
| bufferLength | Size of the buffer in bytes |
| buffer | Data are copied to this buffer |

## Example

```c
void OnAREthMessage( dword messageHandle )
{
  BYTE buffer[200];
  BYTE bufferMsg[200];
  dword count;
  dword size;
  CHAR dest[200];

  count = 0;

  // Check if message is a non Service Discovery message
  if(AREthGetMessageId(messageHandle) != 0xFFFF8100)
  {
    // Check if message is a Notification message
    if(AREthGetMessageType(messageHandle) == 0x2)
    {
      write("SOME/IP Notification message reveived!\n");

      // write whole message data (including header and payload) to write window
      size = AREthSerializeMessage(messageHandle,elcount(bufferMsg),bufferMsg);
      write("Message size: %d",size);
      snprintf(dest, elcount(dest), "%s","");
      for(count = 0; count < size; count++)
      {
        snprintf(dest, elcount(dest), "%s %02x",dest,bufferMsg[count]);
      }
      write("Serialized Message: %s",dest);

      // write only message payload to write window
      size = AREthGetData(messageHandle,elcount(buffer),buffer);
      write("Payload size: %d",size);
      snprintf(dest, elcount(dest), "%s","");
      for(count = 0; count < size; count++)
      {
        snprintf(dest, elcount(dest), "%s %02x",dest,buffer[count]);
      }
      write("Serialized Payload: %s\n",dest);
    } // if
  } // if
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2 | — | — | — | 2.1 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
