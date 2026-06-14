# DoIP_SetTesterUdpPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetTesterUdpPort( dword port);
```

## Description

Sets the UDP port (UDP_TEST_EQUIPMENT_LISTEN) to be used by the DoIP layer.

This function must be called in on preStart.

## Return Values

—

## Example

```c
dword port;
port = DiagGetCommParameter( "DoIP.TESTER_UDP_Data");
// Set the tester UDP port
DoIPSetTesterUdpPort( port);
```

## Availability

| Since Version |
|---|
