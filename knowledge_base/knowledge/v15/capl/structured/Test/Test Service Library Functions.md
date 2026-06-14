# Test Service Library Functions

> Category: `Test` | Type: `notes`

## Description

Test Functionality | Test Concept

| TEST SERVICE LIBRARY |
|---|

| Functions | Short Description |
|---|---|
| Types of functions | Check functions shall be identifiable easily. So the functions are to be prefixed. |
| Status Report functions | In order to query information about a check, generic and check specific status report functions are implemented. |
| Stimulus functions | Stimulus Generators allow the user to stimulate signals or environment variables - referred to as data sinks in the following - according to a specific time behavior. |
| Check overview | Each function specification ChkStart_ implies a specification of a ChkCreate_ function. This ChkStart_ function creates and additionally starts the check. |
| Commands to control checks | These functions can be used to turn off checking in not relevant time, and to continue checking. The control functions can also be used to setup dependencies between checks. |
| Configuration Functions | The ChkConfig* functions permit configuration of the TestServiceLibrary. |
| Error codes | For all status report functions, the return values and raised error classes are applied. |

| Version 15© Vector Informatik GmbH |
|---|
