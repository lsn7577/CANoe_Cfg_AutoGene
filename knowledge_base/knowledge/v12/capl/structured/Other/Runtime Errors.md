# Runtime Errors

> Category: `Other` | Type: `notes`

## Description

A number of runtime errors are monitored:

If a runtime error is detected the function runError is called. This outputs a comment to the Write Window, which contains the name of the CAPL program, the type of error and an error index. With the help of the error index, the point in the CAPL source text which generated the error is found. Measurement is terminated after output of the comment.

The user can also call the function runError directly to generate assertions.
