# linMeasEdgeTimeDiffs

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linMeasEdgeTimeDiffs(dword numIndices, long indices[]); // form 1
```

## Description

This function activates the measurement of the falling edges of the specified bytes in the next frame with the correct id if specified. If the first form is used (without specifying an id), or by specifying the id 0xff/-1, the measurement takes place in the next frame.

The measured values can be queried with linGetMeasEdgeTimeDiffs. The bit rates of the measured bytes can be queried via linGetMeasByteBitRates.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// Test case for measuring edges of a number of data bytes of a LIN frame.
// Note: This test case can only be used in the context of test module nodes
testcase tcMeasureEdges(int byteIndex)
{
   long indices[1];
   float timeDiffs[4];
   dword numDiffs;
   indices[0] = byteIndex;
   // 
 set request to measure the edges of the specified byte of the frame with ID=0x33
   linMeasEdgeTimeDiffs(1, indices, 0x33);
   // 
 wait maximum 1000 [ms] for frame with ID=0x33
   waitResult = TestWaitForMessage(0x33, 1000);
   // declare failure if Wait has resumed not due to expected event
   if (1 != waitResult)
   {
      TestStepFail("Test1.1","Expected frame has not occurred during 1000 ms!");
   }
   // retrieve measured edges
   numDiffs = LINGetMeasEdgeTimeDiffs(4, timeDiffs);
   if (numDiffs == 0)
   {
      TestStepFail("Test1.1", "Failed to measure edges!");
   }
   else
   {
      TestStepPass("Test 1.1", "Edge measurement done...");
   }
}
```

## Availability

| Since Version |
|---|
