# J1939TxReqPG

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939TxReqPG( dword ecuHandle, dword pgn, dword destination, dword priority, dword dlc, char data[] );
```

## Description

Sends any PG. The node layer handles fragmenting automatically. As soon as the PG has been transferred, J1939TxIndication() is called. This gives the application the possibility of protocol monitoring, especially in the case of fragmented PGs.

It should be noted with this function that the destination address must be transferred in a separate parameter dest for PDU Format I. The PDUS byte of pgNum must therefore contain "00". The PG is then transferred to a specific destination address (as a CMDT if appropriate). In the case of PDU Format II the total PG number is transferred in pgNum. The value in dest will then be ignored. The parameter group is sent globally (in some cases as BAM). In this version, you should note that each immediately sequential, fragmented PG for an ECU cannot be sent until after the TxIndication of the previous one has been received. If the data length fits with the transmission protocol, the return value is "0" and the PGN is sent. Otherwise a non-zero value will be returned and the message will not be transferred.

## Return Values

0 on success or error code

## Example

```c
char data[14];

// global parameter group
res = J1939TxReqPG(ecuHdl, 
 0xFE45, 0xFF, 4, 14, data);

// specific 
 parameter group:
res = J1939TxReqPG(ecuHdl, 0xE600, 0x09, 4, 
 14, data);
```

## Availability

| Since Version |
|---|
