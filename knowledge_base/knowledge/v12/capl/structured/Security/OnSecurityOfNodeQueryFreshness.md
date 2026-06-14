# OnSecurityOfNodeQueryFreshness

> Category: `Security` | Type: `function`

## Syntax

```c
long OnSecurityOfNodeQueryFreshness(char nodeName[], char nameName[], dword context, char pduName[], dword dataId, dword freshnessValueId, dword attemptNr, byte payload[], dword payloadLength, qword& freshness, dword& freshnessLength, qword truncatedRxFreshness, dword truncatedRxFreshnessBitLength)
```

## Description

This callback is called for every secured PDU of the specified node on the specified network for which a CMAC has to be calculated of verified.

The callback is triggered before the CMAC calculation starts.

The callback provides the possibility the calculate a freshness value in CAPL and force the Security Manager to use this freshness value for the next CMAC calculation / verification.

You have to call SecurityLocalStartControlSimulationNode before this callback is called.

## Return Values

qword& freshness [Out]The freshness the CAPL code provides.

## Example

```c
// Example 1:
// implement this callback at the transmitting node of the pdu
// This example shows how to specify an older or newer freshness value, the CMAC will be "correct" but the freshness is "wrong" (compared to the freshness of the system)
long OnSecurityOfNodeQueryFreshness(char nodeName[], char nameName[], dword context, char pduName[], dword dataId, dword freshnessValueId, dword attemptNr, byte payload[], dword payloadLength, qword& freshness, dword& freshnessLength, qword truncatedRxFreshness, dword truncatedRxFreshnessBitLength)
{
  char testNodeName[10]    = "ECU1";
  char testNetworkName[10] = "CAN1";

if((!strncmp(nodeName,testNodeName,strlen(nodeName)))&&(!strncmp(networkName,testNetworkName,strlen(networkName))))
  {
    long result = 0;
    char  idString[2] = "";
    dword idValue;
    BYTE freshnessValue[6];
    dword freshnessValueLength;

    // filter for tx pdus (tx = 0; rx = 1)
    if (context != 0)
    {
      return 0; // use internal freshness model
    }

    // filter for the correct data id to influence
    if (dataId != 0)
    {
      return 0; // use internal freshness model
    }
    // now get the freshness currently stored in the internal freshness model
    // the following parameter size and values are depending on the selected Security Profile.
    // Please refer to the Security Source Manual to get more detailled information
    // about parameter values, identifier and freshness value layouts.

    idValue = 0;
    freshnessValueLength= 6;
    result = SecurityOfNodeGetFreshnes(testNodeName,testNetworkName,"", idValue, freshnessValue, freshnessValueLength);

    // change the freshness value
    freshnessValue[5] = 0xFF;

    // write the new Freshness value back.
    // the last parameter is currently reserved and shall be set to 0
    result = SecurityOfNodeSetFreshnes(testNodeName,testNetworkName,"", idValue, freshnessValue, freshnessValueLength, 0);
  }
  // as Set and Get Freshness is changing the internal freshness model, return 0 
  return 0;
}
// Example 2:
// This example shows how to provide a USER based freshness value
long OnSecurityOfNodeQueryFreshness(char nodeName[], char nameName[], dword context, char pduName[], dword dataId, dword freshnessValueId, dword attemptNr, byte payload[], dword payloadLength, qword& freshness, dword& freshnessLength, qword truncatedRxFreshness, dword truncatedRxFreshnessBitLength)
{
  char testNodeName[10]    = "ECU1";
  char testNetworkName[10] = "CAN1";

if((!strncmp(nodeName,testNodeName,strlen(nodeName)))&&(!strncmp(networkName,testNetworkName,strlen(networkName))))
  {
    if ((dataId == 1) && (context == 0)) // check for PDU with data ID and
    context [(0 = tx) (1 = rx)] to specify a freshness for
    {
      freshness = 7; // new Freshness Value
      freshnessLength = 64; // new freshness length

      return 1; // use my values
    }
  }
  return 0; // for all others use internal calculated freshness values
}
```

## Availability

| Since Version |
|---|
