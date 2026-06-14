# <OnAfdxPacket>

> Category: `ADFX` | Type: `function`

## Syntax

```c
void <OnAfdxPacket>( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet );
```

## Description

This callback is called when a registered AFDX packet is received.

## Return Values

—

## Example

Node System - preStart in CAPL Browser

Node Callback Function in CAPL Browser

```c
on preStart
{
  long result;
  // register a callback to receive AFDX packets in general
  result = AfdxRegisterReceiveCallback("OnAfdxPacket");
}
void OnAfdxPacket(long dir, long line, int64 time, long bag, long afdxFlags, long packet )
{
  // check if the packet has been sent by the node
  if (dir == TX)
  {
    sysSetVariableInt(sysvar::NodeA::TxPacketCount,(SysGetVariableInt(sysvar::NodeA::TxPacketCount) + 1));
  } // if
}
```

## Availability

| Since Version |
|---|
