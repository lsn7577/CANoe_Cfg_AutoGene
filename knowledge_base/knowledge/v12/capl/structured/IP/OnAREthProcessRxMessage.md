# OnAREthProcessRxMessage

> Category: `IP` | Type: `function`

## Syntax

```c
long OnAREthProcessRxMessage(dword messageHandle, long rxChannel);
```

## Description

This callback function is called whenever the IL has received a SOME/IP message.

The return value of this callback determines if the message should be processed by the IL or if it should be ignored. Furthermore the message may be modified before the IL processes the message.

## Return Values

The message will be processed if the callback returns 1.Otherwise the message has been ignored by the callback.

## Example

```c
long OnAREthProcessRxMessage(dword messageHandle, long rxChannel)
{
  DWORD msgId = 0;
  LONG errorCode = 0;
  LONG errorOccured = 0;
  // get data from SOME/IP message
  if((msgId = AREthGetMessageId(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = AREthGetLastError()) != 0)
    {
      write("SOME/IP IL error occured: Error code: %d", errorCode);
      errorOccured = 1;
    } // if
  } // if
  if(errorOccured == 0)
  {
    write("SOME/IP message with Message ID 0x%08x received",msgId);
    return 1;
  } // if
  else
  {
    return 0;
  } // else
}
```

## Availability

| Since Version |
|---|
