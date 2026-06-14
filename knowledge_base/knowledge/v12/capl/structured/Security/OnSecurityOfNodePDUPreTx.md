# OnSecurityOfNodePDUPreTx

> Category: `Security` | Type: `function`

## Syntax

```c
void OnSecurityOfNodePDUPreTx(char nodeName[], char networkName[], char pduName[], dword dataId, byte payload[], dword payloadLength, qword& authInfoHigh, qword& authInfo, dword authInfoBitLength, qword& freshness, dword freshnessBitLength, dword freshnessValueId)
```

## Description

This callback handler is called before the specified node on the specified network transmits a secured PDU, after all data updates and the automatic Authenticator (CMAC) calculation have been done.

Payload, authInfo (Authentication Information) and Freshness can be modified before the transmission starts. By this a fault injection is easily possible.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

byte payload[]The payload of the PDU.

## Example

```c
void OnSecurityOfNodePDUPreTx(char nodeName[], char networkName[], char pduName[], dword dataId, byte payload[], dword payloadLength, qword& authInfoHigh, qword& authInfo, dword authInfoBitLength, qword& freshness, dword freshnessBitLength, dword freshnessValueId)
{
  char testNodeName[10]    = "ECU1";
  char testNetworkName[10] = "CAN1";

if((!strncmp(nodeName,testNodeName,strlen(nodeName)))&&(!strncmp(networkName,testNetworkName,strlen(networkName))))
  {
    if (dataId == 1)
    {
      authInfo = 0x123456; // change cmac
      // freshness = 0x02; // change freshness
      // payload[0] = 0xFF; // change payload;
    }
  }
}
```

## Availability

| Since Version |
|---|
