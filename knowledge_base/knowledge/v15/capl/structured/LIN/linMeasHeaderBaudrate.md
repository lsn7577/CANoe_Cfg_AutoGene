# linMeasHeaderBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
long linMeasHeaderBaudrate(int index);
```

## Description

With this function it is possible to set request to measure the baud rate value for next LIN header event. Channel, where the baud rate is measured, is determined by the CAPL program context.

This function only initiates the baud rate measurement. The result becomes available when the next LIN header occurs and it remains valid until next measurement request. To retrieve the result the function linGetMeasBaudrate() shall be used.

## Parameters

| Name | Description |
|---|---|
| index | This parameter specifies a field of LIN header which will be used for baud rate measurement. 0: Synch field 1: Identifier field |

## Return Values

On successful request returns zero, otherwise -1.

## Example

Test case for measuring baud rate using LIN header event

```c
testcase tcMeasureHeaderBaudrate ()
{
long waitResult, measBaudrate;
// set request to measure baud rate according to Synch 
 field of a LIN header
linMeasHeaderBaudrate(0);
// wait maximum 1000 [ms] for LIN header with identifier 0x33
waitResult = TestWaitForLinHeader(0x33, 1000);
// declare failure if Wait has resumed not due to 
 expected event
if (1 != waitResult)
{
TestStepFail("Test 1.1","No LIN header 
 with ID=0x33 occurred during 1000 ms!");
}
// retrieve measured baudrate
measBaudrate = linGetMeasBaudrate();
if (-1 == measBaudrate)
{
TestStepFail("Test 1.1", "Failed to measure header baudrate!");
}
TestStepPass("Test 1.1", "Header baudrate measurement done...");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.1 | 13.0 | — | — | 1.0 |
| Restricted To | LIN | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
