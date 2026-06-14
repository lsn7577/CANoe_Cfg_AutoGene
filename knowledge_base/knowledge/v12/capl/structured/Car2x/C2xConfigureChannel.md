# C2xConfigureChannel

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xConfigureChannel(long appChannel, long radioChannel, long txPower, long maxTxPower, long layout, long dataRate, long bandWidth, long txAntenna, long rxAntenna)
```

## Description

Configure a hardware channel.

This method allows to redefine some or all channel parameters on the fly, i.e. for all following activities on a specific VN4610 channel those new settings will be used.

In fact the method overwrites the corresponding internal configuration settings provided by the setup-dialog.

Notes:

## Return Values

0 or error code according to the following.

## Example

```c
void configureChannel()
{
  word channelTable[7] = { 172,174,176,178,180,182,184};
  word dataRates[8] = {3,4,6,9,12,18,24,27};
  word currentChannelIndex = 0;
  word currentRateIndex = 0;
  dword errFlag = 0;
  word txPower = 0;

  // loop over all radio channels and data rates per timer callback
  // and configure 2 channels for Tx and Rx

  Write("C2xConfigureChannels radioCh:%d, txPow:%d, dataRate:%d, bandWidth:%d", channelTable[currentChannelIndex], txPower, dataRates[currentRateIndex], 10);
  errFlag = C2xConfigureChannel(1, channelTable[currentChannelIndex], txPower, 25, 1,
    dataRates[currentRateIndex], 10, 1, 1);
  if (errFlag != 0) Write("C2xConfigureChannel #1 failed with err=%d", errFlag);
  errFlag = C2xConfigureChannel(2, channelTable[currentChannelIndex], txPower, 25, 1,
    dataRates[currentRateIndex], 10, 2, 2);
  if (errFlag != 0) Write("C2xConfigureChannel #2 failed with err=%d", errFlag);
}
```

## Availability

| Since Version |
|---|
