# linGetMeasBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
float linGetMeasBaudrate()
```

## Description

With this function it is possible to retrieve results of a last baud rate measurement, which is done by calling linMeasHeaderBaudrate() or linMeasRespBaudrate() functions.

## Return Values

Returns the last measured baud rate [in bit/sec] or -1 on failure.

## Example

Test case for measuring baud rate using certain data byte of a LIN frame.

```c
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

| Since Version |
|---|
