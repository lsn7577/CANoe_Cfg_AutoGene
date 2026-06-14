# DoIP_SendPDUCombination

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_SendPDUCombination();
```

## Description

Send the combined PDUs on the open TCP connection in one block. Typically, the PDUs will be sent in one IP packet, depending on the PDU size of the transporting medium.

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 SP2 | — | — | — | 2.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
