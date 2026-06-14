# linGetResponseData

> Category: `LIN` | Type: `function`

## Syntax

```c
dword LinGetResponseData(linFrame frameObject)
```

## Description

Queries LIN frame response data for specified FrameId on certain LIN channel.

The FrameId and desired LIN channel number are expected to be set in the LIN frameprior to calling this function.

The frame length, dataybte and checksum byte values will be copied into corresponding fields of LIN frame object.

Note, that in the case there is no response data for the specified FrameId no data is copied.

## Return Values

Non-zero on success.Zero on failure or when there is no response data defined.
The non-zero value in real mode is the initial and in simulated mode the actual response counter value.

## Example

```c
on key 'a'
{
   linFrame 0x1 testMsg;
   testMsg.MsgChannel = 1;
   testMsg.ID = 0;
   if (LINGetResponseData(testMsg) > 0)
   {
      writelineex(1,1,"FrameId=%d Length=%d, 0x%X 0x%X 0x%X 0x%X 0x%X 0x%X 0x%X 0x%X;", testMsg.ID,           testMsg.DLC,
      testMsg.byte(0), testMsg.byte(1), testMsg.byte(2), testMsg.byte(3), testMsg.byte(4), testMsg.byte(5), testMsg.byte(6), testMsg.byte(7));
   }
}
```

## Availability

| Since Version |
|---|
