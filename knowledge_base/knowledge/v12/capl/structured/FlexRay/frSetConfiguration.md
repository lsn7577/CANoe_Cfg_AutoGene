# frSetConfiguration

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frSetConfiguration( int channel, <configuration var> );
```

## Description

This function writes the FlexRay protocol parameters from the configuration object to the FlexRay interface's Communication Controller.

The values must previously have been set in the configuration object in compliance with the FlexRay specification.

The new protocol parameters will only be applied when the Communication Controller is reset!

## Return Values

—

## Example

The following CAPL program reconfigures the FlexRay Communication Controller with new FlexRay protocol parameters.

```c
variables
{
   frConfiguration gFRParams;
}
void setFRConf1 ()
{
   frGetConfiguration(%CHANNEL%, gFRParams);
   gFRParams.FRBaudrate = 10000; // "kBit/s"
   gFRParams.gdMacrotick = 1; // "us"
   gFRParams.gMacroPerCycle = 5000; // "MT"
   gFRParams.gdNIT = 100; // "MT"
   //gFRParams.gdSampleClockPeriod = 0.0; // "us"
   gFRParams.gdTSSTransmitter = 10; // "Bit"
   gFRParams.gPayloadLengthStatic = 2; // "Words"
   gFRParams.gdActionPointOffset = 9; // "MT"
   gFRParams.gdStaticSlot = 35; // "MT"
   gFRParams.gNumberOfStaticSlots = 60; // "#"
   gFRParams.gdMinislotActionPointOffset = 4; // "MT"
   gFRParams.gdMinislot = 10; // "MT"
   gFRParams.gNumberOfMinislots = 276; // "#"
   //gFRParams.gClusterDriftDamping = 0; // ""
   gFRParams.gListenNoise = 10; // ""
   gFRParams.gColdStartAttempts = 20; // "#"
   gFRParams.gSyncNodeMax = 4; // "#"
   gFRParams.gOffsetCorrectionStart = 4931; // "MT"
   gFRParams.gdDynamicSlotIdlePhase = 1; // "MS"
   gFRParams.gdSymbolWindow = 35; // "MT"
   gFRParams.gdCASRxLowMax = 0; // "Bit"
   gFRParams.gdCASRxLowMin = 0; // "Bit"
   gFRParams.gdWakeupSymbolRxIdle = 59; // "Bit"
   gFRParams.gdWakeupSymbolRxLow = 51; // "Bit"
   gFRParams.gdWakeupSymbolRxWindow = 301; // "Bit"
   gFRParams.gdWakeupSymbolTxIdle = 180; // "Bit"
   gFRParams.gdWakeupSymbolTxLow = 60; // "Bit"
   gFRParams.gMaxWithoutClockCorrectionFatal = 10; // "double cycles"
   gFRParams.gMaxWithoutClockCorrectionPassive = 6; // "double cycles"
   gFRParams.gNetworkManagementVectorLength = 0; // "Bytes"
   gFRParams.pChannels = 3; // "A+B"
   gFRParams.pMicroPerCycle = 200000; // "uT"
   gFRParams.pSamplesPerMicrotick = 2; // "#"
   gFRParams.pPayloadLengthDynMax = 10; // "Words"
   gFRParams.pPayloadLengthFIFO = 10; // "Words"
   gFRParams.pLatestTx = 272; // "MS"
   gFRParams.pdMaxDrift = 89; // "uT"
   gFRParams.pdAcceptedStartupRange = 189; // "uT"
   gFRParams.pdListenTimeout = 401202; // "uT"
   gFRParams.pClusterDriftDamping = 1; // "uT"
   gFRParams.pDecodingCorrection = 52; // "uT"
   gFRParams.pDelayCompensation_A = 10; // "uT"
   gFRParams.pDelayCompensation_B = 10; // "uT"
   gFRParams.pOffsetCorrectionOut = 143; // "uT"
   gFRParams.pRateCorrectionOut = 601; // "uT"
   gFRParams.pExternOffsetCorrection = 0; // "uT"
   gFRParams.pExternRateCorrection = 0; // "uT"
   gFRParams.pExternCorrectionMode = 0; // ""
   gFRParams.pMacroInitialOffset_A = 9; // "MT"
   gFRParams.pMacroInitialOffset_B = 9; // "MT"
   gFRParams.pMicroInitialOffset_A = 18; // "uT"
   gFRParams.pMicroInitialOffset_B = 18; // "uT"
   gFRParams.pWakeupChannel = 1; // 1 (A) or 2 (B)
   gFRParams.pWakeupPattern = 0; // "#"
   gFRParams.pAllowHaltDueToClock = 1; // "Boolean"
   gFRParams.pAllowPassiveToActive = 1; // "cycles"
   //gFRParams.pBGTick = 0; // "Boolean"
   //gFRParams.pPhysicalLayer = 0; // ""
   gFRParams.pSingleSlotEnabled = 0; // "Boolean"
   //gFRParams.pBGEnable = 0; // "Boolean"
   //gFRParams.pDynamicSegmentEnable = 0; // "Boolean"

   frSetConfiguration(%CHANNEL%, gFRParams);
   resetFlexRayCC(%CHANNEL%); // in order to apply the new values
}
```

## Availability

| Since Version |
|---|
