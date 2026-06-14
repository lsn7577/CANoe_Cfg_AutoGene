# A664InitICMP

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664InitICMP (a664Frame aFrame, dword InitType, word payloadSize, dbNode NodeName) (1)
```

## Description

The complete Ethernet and IP headers of an AFDX packet are consistently set based on the given parameters. With calling convention (1), the initialization values are given in the attributes of a DBC object. Calling convention (2) is intended for full user-control of all the parameters. In this case, it is necessary to configure the corresponding VL, too. Otherwise the VL definition is not complete and it is not possible to schedule the ICMP frame. Use the function A664VLConfig for setting detailed VL parameters.

The IP payload area is initialized according to the parameter InitType. There are three different values possible for this parameter.

The InitType = SWAP_ADR is intended for creating the ECHO REPLY out of a received packet. In this case the parameter payloadSize is ignored. The IP addresses (contents of the selectors IpAdrDst and IpAdrSrc) are swapped. ICMP type and code are set to ECHO REPLY.

(1) The VL for the packet is taken from the DBC attribute ICMP_outVLid and the MAC addresses are adapted accordingly. Note that the ICMP payload is not modified.

(2) The parameters srcIP and dstIP are ignored. The VL for the packet is taken from parameter VLid and the MAC addresses are adapted accordingly. Note that the ICMP payload is not modified.

The values InitType = ECHO_REPLY or PING_REQ are used to initialize a newly created packet. The ICMP payload area is created according to payloadSize and set to 0. Furthermore ICMP type and code are set.

(1) The source IP address (selector IpAdrSrc) is taken from the initialization file CAN.INI (section = AFDX; value = DefaultSrcIP). The VL-related configuration is given from the DBC object.

(2) The function provides the complete addressing information. Note that the function A664VLConfig() has to be called for setting detailed VL parameters.

Note: A multicast IP address value is not allowed for ICMP.

## Example

includes{ #include "AFDX/utils.cin"}…on key 'p' // generate ping-request using DBC info{ a664Frame *fr = { msgChannel = 1 }; // use equipment info og LI_SDF_3 from DBC to specify icmp- configuration a664InitICMP(fr, PING_REQ, LI_SDF_3.ICMP_outVLbufSize, LI_SDF_3); a664TriggerFrame(fr, 1); // single shot, but respect BAG}

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

| Since Version |
|---|
