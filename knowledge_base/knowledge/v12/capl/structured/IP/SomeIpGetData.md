# SomeIpGetData

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetData( dword messageHandle, dword bufferLength, char buffer[] );
```

## Description

This function can be used to query the raw data of a SOME/IP message.

## Return Values

0: An error occurred. The error can be evaluated using the SomeIpGetLastError function.

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  BYTE buffer[200];
  BYTE bufferMsg[200];
  DWORD count;
  DWORD size;
  CHAR dest[200];

  count = 0;

  // Check if message is a non Service Discovery message
  if(SomeIpGetMessageId(messageHandle) != 0xFFFF8100)
  {
    // Check if message is a Notification message
    if(SomeIpGetMessageType(messageHandle) == 0x2)
    {
      write("SOME/IP Notification message reveived!\n");

      // write whole message data (including header and payload) to write window
      size = SomeIpSerializeMessage(messageHandle,elcount(bufferMsg),bufferMsg);
      write("Message size: %d",size);
      snprintf(dest, elcount(dest), "%s","");
      for(count = 0; count < size; count++)
      {
        snprintf(dest, elcount(dest), "%s %02x",dest,bufferMsg[count]);
      }
      write("Serialized Message: %s",dest);

      // write only message payload to write window
      size = SomeIpGetData(messageHandle,elcount(buffer),buffer);
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

| Since Version |
|---|
