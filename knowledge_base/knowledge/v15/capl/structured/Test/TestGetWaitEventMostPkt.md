# TestGetWaitEventMostPkt

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitEventMostPkt();
long TestGetWaitEventMostPkt(dword aIndex);
```

## Description

If the last (single) wait condition was resolved by a MOST packet event, the first function makes the packet data accessible by the packet API functions normally used within the onMostPkt() event handler, such as mostPktSrcAdr(), mostPktDestAdr(), mostPktGetData() etc.

The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

Once another wait condition is set up in the current test sequence, access to the packet data will be no longer available.

## Parameters

| Name | Description |
|---|---|
| aIndex | Number of the “joined event” that was resumed by a MOST packet event. The number corresponds to return value of the "testJoin..." function call, by which the event was added to a joined condition. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | — |
| Restricted To | — | MOST25, MOST50, MOST150 | MOST25, MOST50, MOST150 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
