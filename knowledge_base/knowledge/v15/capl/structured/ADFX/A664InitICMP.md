# A664InitICMP

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664InitICMP (a664Frame aFrame, dword InitType, word payloadSize, dbNode NodeName) (1)
long A664InitICMP (a664Frame aFrame, dword InitType, word payloadSize, dword srcIP, dword dstIP, word VLid) (2)
```

## Description

The complete Ethernet and IP headers of an AFDX packet are consistently set based on the given parameters. With calling convention (1), the initialization values are given in the attributes of a DBC object. Calling convention (2) is intended for full user-control of all the parameters. In this case, it is necessary to configure the corresponding VL, too. Otherwise the VL definition is not complete and it is not possible to schedule the ICMP frame. Use the function A664VLConfig for setting detailed VL parameters.

The IP payload area is initialized according to the parameter InitType. There are three different values possible for this parameter.

## Parameters

| Name | Description |
|---|---|
| aFrame | The frame object to be initialized |
| InitType | 1: ECHO_REPLY: initializes the type/code to ECHO REPLY 8: PING_REQ: initializes the type/code to PING REQUEST 256: SWAP_ADR: swaps addressing information (source/destination MAC and IP addresses), initializes the type/code to ECHO REPLY, the parameter payloadSize is ignored |
| payloadSize | size of the optional ICMP payload places after the ICMP header (corresponds to the bytes in IpPayload following the ICMP header). The valid range is [0 .. ICMP_outVLbufSize / ICMP_inVLbufSize] This parameter is ignored if InitType is set to SWAP_ADR. |
| NodeName | (1) This is the name of a node from the assigned DBC. The DBC must be an AFDX DBC file and the necessary attributes must exist. |
| srcIP | (2) source IP address to be used for the Eth- and IP-headers. This parameter is ignored if InitType is set to SWAP_ADR. |
| dstIP | (2) destination IP address to be used for the IP-headers. This parameter is ignored if InitType is set to SWAP_ADR. |
| VLid | (2) VLId to be used for the destination Eth-header (see selector EthVlId) |

## Example

Create ICMP frames from DBC attributes

Create ICMP frames manually

```c
includes
{
  #include "AFDX/utils.cin"
}
….
on key 'P'  // generate ping-request manually
{
  a664Frame *fr = { msgChannel = 1 };
  DWORD srcIP, dstIP;
  srcIP = IpGetAddressAsNumber("10.1.38.1");
  dstIP = IpGetAddressAsNumber("10.2.38.2");
  a664InitICMP(fr, PING_REQ, 16, srcIP, dstIP, 6673);
  a664TriggerFrame(fr, 1);	  // single shot, but respect BAG
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
