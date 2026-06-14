# linMeasHeaderBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
long linMeasHeaderBaudrate(int index)
```

## Description

With this function it is possible to set request to measure the baud rate value for next LIN header event. Channel, where the baud rate is measured, is determined by the CAPL program context.

This function only initiates the baud rate measurement. The result becomes available when the next LIN header occurs and it remains valid until next measurement request. To retrieve the result the function linGetMeasBaudrate() shall be used.

When LIN hardware is in Master mode calling this function will have no effect.

The baud rate can only be measured if the specified byte (PID or Sync Byte) contains at least one "0"-bit followed by a "1"-bit. This means that bytes with the following values cannot be measured:

0x0 (binary: 00000000)0x80 (binary: 10000000)0xC0 (binary: 11000000)0xE0 (binary: 11100000)0xF0 (binary: 11110000)0xF8 (binary: 11111000)0xFC (binary: 11111100)0xFE (binary: 11111110)0xFF (binary: 11111111)

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

| Since Version |
|---|
