# TestGetWaitEventMostPkt

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitEventMostPkt();
```

## Description

If the last (single) wait condition was resolved by a MOST packet event, the first function makes the packet data accessible by the packet API functions normally used within the onMostPkt() event handler, such as mostPktSrcAdr(), mostPktDestAdr(), mostPktGetData() etc.

The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

Once another wait condition is set up in the current test sequence, access to the packet data will be no longer available.

## Return Values

0: Successful data access

## Example

```c
// Access to packet data:
  if(testWaitForMostPkt("AudioDiskPlayer.MediaInfo.Status", 1, 500) == 1)
  {
    byte data[1524];
    long pktSize;
    testGetWaitEventMostPkt();
    pktSize = mostPktGetData(data, elCount(data));
    if(pktSize > 5)
    {
      testStepPass("Packet test", "%d bytes received", pktSize);
    }
    else
    {
      testStepFail("Packet test");
    }
  }
```

## Availability

| Since Version |
|---|
