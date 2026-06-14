# OnTcpSend

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnTcpSend( dword socket, long result, char buffer[], dword size);
```

## Description

If the CAPL program implements this callback it is called when the data from the stack have been processed but not yet placed on the bus. The information is first displayed in the CANoe Trace Window when it has physically been sent.

## Return Values

—

## Example

```c
// ---------------------------------------------------
// When asynchronous TcpSend is complete...
// ---------------------------------------------------
void OnTcpSend( dword socket, long result, char buffer[], dword size)
{
  if (socket != ~0)
  {
    // sending data complete.
    If (result != 0)
    {
      writeLineEx(1, 3, “OnTcpSend error: %d”, result);
    }
  }
}
```

## Availability

| Since Version |
|---|
