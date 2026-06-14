# linMeasRespBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
long linMeasRespBaudrate(long frameID, int index);
```

## Description

With this function it is possible to send a request to measure the baud rate value of a certain data byte of a certain LIN frame. The channel where the baud rate is measured is determined by the CAPL program context.

This function only initiates the baud rate measurement. The result becomes available when the next bus event for the specified ID occurs and it remains valid until the next measurement request. To retrieve the result the function linGetMeasBaudrate() shall be used.

## Parameters

| Name | Description |
|---|---|
| frameID | LIN frame identifier whose baud rate will be measured. Value range: 0…63 |
| index | Data byte index. Value range: 0..N, where N = length [in bytes] of specified LIN frame [0..N-1]: data bytes 1..N N: checksum byte |

## Return Values

On successful request returns zero, otherwise -1.

## Example

Test case for measuring baud rate using certain data byte of a LIN frame.

```c
testcase tcMeasureDatabyteBaudrate (int byteIndex)
{
long waitResult, measBaudrate;
// set request to measure baud rate using the specified byte of a frame with ID=0x33
linMeasRespBaudrate(0x33, byteIndex);
// wait maximum 1000 [ms] for a frame with ID=0x33
waitResult = TestWaitForMessage(0x33, 1000);
// declare failure if Wait has resumed not due to expected event
if (1 != waitResult) {
TestStepFail("Test 1.1","Expected frame has not occurred during 1000 ms!");
}
// retrieve measured baudrate
measBaudrate = linGetMeasBaudrate();
if (-1 == measBaudrate)
{
TestStepFail("Test 1.1", "Failed to measure response baudrate!");
}
TestStepPass("Test 1.1", "Response baudrate measurement done...");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.1 | — | — | — | 1.0 |
| Restricted To | LIN Real bus mode | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
