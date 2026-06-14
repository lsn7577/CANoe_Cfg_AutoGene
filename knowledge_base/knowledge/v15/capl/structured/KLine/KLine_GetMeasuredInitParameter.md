# KLine_GetMeasuredInitParameter

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_GetMeasuredValue(dword parameterID)
```

## Description

Retrieves the different parameters of the init patterns.

## Parameters

| Name | Description |
|---|---|
| parameterID | Value range: 0-10 0: KeyByte11: Keybyte22: TiniL3: Twup4: W4 between key byte 2 and inverted key byte 25: W16: W27: W38: W49: W4 between inverted keybyte 2 and inverted address byte10: BaudRate from sync pattern |

## Return Values

Parameter value or error code.

## Example

```c
DiagRequest StartDiagnosticSession req;
enum eMeasuredValues
{
   KeyByte1            = 0,
   KeyByte2            = 1,
   TiniL               = 2,
   Twup                = 3,
   W4Time1             = 4,
   InvertedAddressByte = 5,
   W1Time              = 6,
   W2Time              = 7,
   W3Time              = 8,
   W4Time2             = 9,
   BaudRateSyncByte    = 10
};

long pKeyByte1;
long pKeyByte2;
long pW4Time1;
long pInvertedAddressByte;
long pW1Time;
long pW2Time;
long pW3Time;
long pW4Time2;
long pBaudRateSyncByte;

DiagSetTarget(“DUT”);
DiagConnectChannel();
   if (1 == TestWaitForDiagChannelConnected(3000))
   {
      TestStepPass("Channel connected successfully");
   }
   else
   {
      TestStepFail("Could not connect channel");
   }

req.SendRequest();
   if (1 == testWaitForDiagKLineFrameTransmitted(1000))
   {
      TestStepPass("Request transmitted successfully.");
   }
   else
   {
      TestStepFail("No request transmitted.");
   }

pKeyByte1 = KLine_GetMeasuredInitParameter(KeyByte1);
pKeyByte2 = KLine_GetMeasuredInitParameter(KeyByte2);
pW4Time1 = KLine_GetMeasuredInitParameter(W4Time1);
pInvertedAddressByte = KLine_GetMeasuredInitParameter(InvertedAddressByte);
pW1Time = KLine_GetMeasuredInitParameter(W1Time);
pW2Time = KLine_GetMeasuredInitParameter(W2Time);
pW3Time = KLine_GetMeasuredInitParameter(W3Time);
pW4Time2 = KLine_GetMeasuredInitParameter(W4Time2);
pBaudRateSyncByte = KLine_GetMeasuredInitParameter(BaudRateSyncByte);

write("KeyByte1: 0x%x", pKeyByte1);
write("KeyByte2: 0x%x", pKeyByte2);
write("W4Time 1: %.2f", pW4Time1/toMs);
write("InvertedAddressByte: 0x%x", pInvertedAddressByte);
write("W1Time: %.2f", pW1Time/toMs);
write("W2Time: %.2f", pW2Time/toMs);
write("W3Time: %.2f", pW3Time/toMs);
write("W4Time 2: %.2f", pW4Time2/toMs);
write("BaudRateSyncByte: %d", pBaudRateSyncByte);

DiagCloseChannel();
   if (1 == testWaitforDiagChannelClosed(1000))
   {
      TestStepPass("Diag channel closed successfully");
   }
   else
   {
      TestStepFail("Diag channel could not be closed.");
   }
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | — | — | — | 1.1 SP2 |
| Restricted To | K-Line Real bus mode ECU tester | K-Line Real bus mode ECU tester | — | — | — | K-Line Real bus mode ECU tester |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
