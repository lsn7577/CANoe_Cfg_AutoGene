# DoIP_SendPDUCombination

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_SendPDUCombination();
```

## Description

Send the combined PDUs on the open TCP connection in one block. Typically, the PDUs will be sent in one IP packet, depending on the PDU size of the transporting medium.

## Return Values

-11: Sending data on the TCP connection failed

## Example

```c
BYTE rawReq[7] = {
  0x01, 0x01 // target address (ECU)
, 0x0E, 0x80 // source address (tester)
, 0x22, 0x01, 0x05 // diagnostics service Read Data By Identifier
};

// Initialize the PDU combination, i.e. drop previous combination
DoIP_CreatePDUCombination();

// Add diagnostics message PDUs, changing the target address for each PDU
DoIP_AddCombinedPDU( 0x8001, rawReq, 7);
rawReq[1] = 0x02;
DoIP_AddCombinedPDU( 0x8001, rawReq, 7);
rawReq[1] = 0x03;
DoIP_AddCombinedPDU( 0x8001, rawReq, 7);
rawReq[1] = 0x04;
DoIP_AddCombinedPDU( 0x8001, rawReq, 7);

// Send the PDU combination. On Ethernet all four PDUs will be put into the
// same frame and arrive together at the DoIP gateway
DoIP_SendPDUCombination();
```

## Availability

| Since Version |
|---|
