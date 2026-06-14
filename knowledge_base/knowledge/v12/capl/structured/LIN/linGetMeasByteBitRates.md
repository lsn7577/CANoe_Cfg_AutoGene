# linGetMeasByteBitRates

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetMeasByteBitRates(dword arrSize, float byteBitRates[]);
```

## Description

This function calculates the bit rates for every byte which has been selected for edge time measurement. It uses the received data as well as the measured edge differences. Therefore, the function linMeasEdgeTimeDiffs must be called in advance. Note that for each measured byte a bit rate will be returned, although it might be 0 (this happens if there had been only one falling edge in the measured byte).

## Return Values

Returns the number of bit rates copied into the byteBitRates-array.

## Example

```c
testcase ByteBitRatesTest()

{
  long indices[2] = { -2, -1 };
  float byteBitRates[2];
  dword numByteBitRates, i;
  char variableDesc[32];

  // start a new edge difference measurement for the next frame
  if (linMeasEdgeTimeDiffs(2, indices) == 0)
  {
    TestStepFail("ByteBitRatesTest", "Starting of edge measurement failed.");
    return;
  }

  // wait for any lin header
  if (testWaitForLinHeader(1000) != 1)
  {
    TestStepFail("ByteBitRatesTest", "No LIN header received within 1000 ms.");
    return;
  
}
  // receive the measured bit rates
  numByteBitRates = linGetMeasByteBitRates(elCount(byteBitRates), byteBitRates);
  if (numByteBitRates != elCount(indices))
  {
    TestStepFail("ByteBitRatesTest", "Received implausible number of bit rates.");
    return;
  }
  for (i = 0; i < numByteBitRates; i++)
  {
    snprintf(variableDesc, elCount(variableDesc), "Bit rate of byte %d", indices[i]);
    testCaseReportMeasuredValue(variableDesc, byteBitRates[i], "bit/s");
  }
  TestStepPass("ByteBitRatesTest", "All byte bit rates have been received.");
}
```

## Availability

| Since Version |
|---|
