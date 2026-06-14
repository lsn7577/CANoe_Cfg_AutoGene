# linGetMeasBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
float linGetMeasBaudrate();
```

## Description

With this function it is possible to retrieve results of a last baud rate measurement, which is done by calling linMeasHeaderBaudrate() or linMeasRespBaudrate() functions.

## Return Values

Returns the last measured baud rate [in bit/sec] or -1 on failure.

## Example

Example 1

Test case for measuring baud rate using LIN header event.

These test cases can only be used in the context of test module nodes.

Example 2

Test case for measuring baud rate using certain data byte of a LIN frame.

```c
testcase tcMeasureHeaderBaudrate ()
{
long waitResult, measBaudrate;
// set request to measure baud rate according to Synch field of a LIN header
linMeasHeaderBaudrate(0);
// wait maximum 1000 [ms] for LIN header with identifier 0x33
waitResult = TestWaitForLinHeader(0x33, 1000);
// declare failure if Wait has resumed not due to expected event
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
testcase tcMeasureDatabyteBaudrate (int byteIndex)
{
long waitResult, measBaudrate;
// set request to measure baud rate using the specified 
 byte of a frame with ID=0x33
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
