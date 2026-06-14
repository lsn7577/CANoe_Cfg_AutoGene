# Assigning and Creating Bitmaps

> Category: `Panel` | Subcategory: `General` | Type: `concept`

You can create and edit bitmap files with any bitmap editor (e.g. Paint, Photoshop).

A bitmap file for a n-stage switch always consists of n+1 rectangular partial bitmaps, each with the same height and width, arranged to be horizontally adjacent to one another.

In the first rectangle the inactive state is shown. This appears on the panel when no symbol has been assigned to the element. The Switch/Indicator shows the inactive state as long as the assigned Signal will be received.

The n switch values are located in the n partial bitmaps to the right of this.

Example of Two-Stage Switch

Note

When creating your own bitmaps be sure to save them as uncompressed Windows bitmaps. Some graphics drivers cannot process specially compressed bitmaps, which may result in undesirable optical effects or even system crashes.

It is advisable to save all bitmaps belonging to a panel in a separate subdirectory. If you wish to forward a panel to another user you must also forward the bitmap directory.

| Example of Two-Stage Switch |
|---|

| Note When creating your own bitmaps be sure to save them as uncompressed Windows bitmaps. Some graphics drivers cannot process specially compressed bitmaps, which may result in undesirable optical effects or even system crashes. It is advisable to save all bitmaps belonging to a panel in a separate subdirectory. If you wish to forward a panel to another user you must also forward the bitmap directory. |
|---|
