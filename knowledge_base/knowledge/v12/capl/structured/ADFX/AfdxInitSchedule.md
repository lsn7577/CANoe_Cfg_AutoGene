# AfdxInitSchedule

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxInitSchedule( long packet );
```

## Description

Initializes the scheduled transmission of the specified message during the start phase of the measurement.

The behavior of the function call differs for different measurement phases.

## Return Values

0 or error code

## Example

```c
on preStart
{
  long packet;
  char errTxt[256];

  packet = AfdxInitPacket(0, "TESTMSG_ALLTYPES", 0 );
  if (packet == 0)
  {
    AfdxGetLastErrorText(elCount(errTxt), errTxt);
    writeEx( -3, 0, "<%NODE_NAME%> AfdxInitPacket failed due to:%s", errTxt );
  }

  if (AfdxInitSchedule(packet) != 0)
  {
    AfdxGetLastErrorText(elCount(errTxt), errTxt);
    writeEx( -3, 0, "<%NODE_NAME%> AfdxInitSchedule failed due to:%s", errTxt );
  }
  AfdxReleasePacket(packet);
}
```

## Availability

| Since Version |
|---|
