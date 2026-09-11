`NaN != NaN` wasn't an oversight. Kahan put it in IEEE 754 deliberately: before `isnan()` existed, comparing a value against itself was the cheapest NaN check available. One instruction, no library.
