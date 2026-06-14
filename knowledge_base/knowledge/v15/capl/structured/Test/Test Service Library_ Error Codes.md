# Test Service Library: Error Codes

> Category: `Test` | Type: `notes`

## Description

For all status report functions, the following return values and raised error classes are applied. The query functions always use a wider range of return values. In most cases the particular check of the return value isn't necessary. A simple check to a value >0 (stands for valid) is enough.

Please refer the specification of each query function to get the complete value range of return values.

| Return Values | Return Value Meanings and Raised Error Class |
|---|---|
| 0 | Query has been performed successfully |
| -1 | Check does not existClass: Access to non-existing check |
| -2 | Check does not support this queryClass: Invalid query on check |
| -3 | The Check was never activeClass: Invalid query on check |
| -4 | No event has occurredClass: Information |
| -5 | Pointer to CAPL-Argument is NULLClass: Invalid test specification |
| -6 | There are multiple objects that match on this queryClass: Ambiguous query. Multiple objects match on this query |
| -7 | Node layer module is deactivated and cannot process the query |

| Version 15© Vector Informatik GmbH |
|---|
