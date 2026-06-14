# diagSetTarget

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetTarget (char ecuName[])
```

## Description

Sets the target ECU with which the tester shall communicate from now on and configures/establishes the communication channel to that ECU.

After calling the function in the tester, the following actions are executed:

## Return Values

Error code

## Example

```c
// In this example, diagSetTarget(<ECU>) is simply called once in the
// ‘MainTest’ function of a test node, as this tester only needs to access
// one dedicated ECU with ECU qualifier "Door".
// In case a test module needs to perform diagnostics with different ECUs,
// the function could be called e.g. in the first / initializing test case
// of a test group for each specific ECU

void MainTest ()
{
  if( 0 != diagSetTarget( "Door")) write( "Error setting target!");
  // ... Call your test cases here
}
```

## Availability

| Since Version |
|---|
