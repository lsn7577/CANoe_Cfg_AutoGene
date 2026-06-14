# TestGetWaitEventKLineByte

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetKLineByte();
long TestGetKLineByte(int64 timeStampOut);
```

## Description

If a byte is the last event that triggers a wait instruction, the content can be called up with the first function.

The second function allows to call the content and the end of byte time stamp.

## Parameters

| Name | Description |
|---|---|
| timeStampOut | End of byte time stamp. |

## Return Values

Value of the byte

## Example

```c
DiagRequest EcuIdentification_Read req;
int64 timeStamps;
Byte byteValue;

DiagSetTarget(“DUT”);
req.SendRequest();

   if (1 == TestWaitForDiagKLinebyteTransmitted(5000))
   {
      TestStepPass("Transmitted KLine frame.");
      byteValue =  TestGetWaitEventKLineByte( timeStamp) ;
      write( "TRANSMITTED BYTE VALUE: 0x%x. TIMESTAMP [%.3f]", byteValue, timeStamp/1000000000.0);
   }
   else
   {
   TestStepFail("No confirmation of transmitted K-Line byte.");
   }
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | 1.0 |
| Restricted To | — | K-Line Real bus mode | — | — | — | K-Line Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
