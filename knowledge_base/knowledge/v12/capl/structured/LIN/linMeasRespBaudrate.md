# linMeasRespBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
long linMeasRespBaudrate(long frameID, int index)
```

## Description

With this function it is possible to send a request to measure the baud rate value of a certain data byte of a certain LIN frame. The channel where the baud rate is measured is determined by the CAPL program context.

This function only initiates the baud rate measurement. The result becomes available when the next bus event for the specified ID occurs and it remains valid until the next measurement request. To retrieve the result the function linGetMeasBaudrate() shall be used.

The baud rate can only be measured if the specified data byte contains at least one "0"-bit followed by a "1"-bit. This means that bytes with the following values cannot be measured:

0x0 (binary: 00000000)0x80 (binary: 10000000)0xC0 (binary: 11000000)0xE0 (binary: 11100000)0xF0 (binary: 11110000)0xF8 (binary: 11111000)0xFC (binary: 11111100)0xFE (binary: 11111110)0xFF (binary: 11111111)

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

| Since Version |
|---|
