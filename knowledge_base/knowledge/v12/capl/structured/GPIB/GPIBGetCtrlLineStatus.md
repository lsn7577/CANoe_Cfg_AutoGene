# GPIBGetCtrlLineStatus

> Category: `GPIB` | Type: `function`

## Syntax

```c
long GPIBGetCtrlLineStatus (long boardIdx);
```

## Description

Returns the status of the GPIB control lines.

## Return Values

Line Status Bytes
The value consists of 2 bytes. The low-order byte (bits 0 through 7) contains a mask indicating the capability of the GPIB interface to sense the status of each GPIB control line. The high-order byte (bits 8 through 15) contains the GPIB control line state information. If a bit is set (1), the corresponding control line can be monitored by the interface or is asserted, respectively. The following is a pattern of each byte.
7
6
5
4
3
2
1
0
EOI
ATN
SRQ
REN
IFC
NRFd
NDAC
DAV

## Availability

| Since Version |
|---|
