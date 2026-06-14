# coTfsGuarding

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsGuarding( void );
```

## Description

This test checks the life guarding and node guarding functionality of the node.

The life guarding tests are executed with the following parameters:

guard time: 1s, 500ms, 500ms

retry factor: 3, 5, 3

permissible tolerance: 10%, 10%, 5%

After that, the node guarding tests with decreasing time tolerances are executed to check the response time. The permissible deviations are 500 ms, 10 ms, 50 ms and 26 ms. To pass the test, all individual test cases must be run through successfully.

## Return Values

Error code

## Example

```c
if (coTfsGuarding() != 1) {
  write( "guarding test failed");
}
```
