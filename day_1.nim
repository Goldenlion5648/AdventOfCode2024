import sugar
import std/strutils
import sequtils
import algorithm
import tables

let contents = readFile("input1.txt").strip
var left = collect:
    for line in contents.splitLines:
        line.split(" ")[0].parseInt
        
var right = collect:
    for line in contents.splitLines:
        line.split(" ")[^1].parseInt
        
left.sort()
right.sort()

var part1Answer = 0
for i in 0..<left.len:
    part1Answer += abs(left[i] - right[i])
echo "Part 1:", part1Answer

var rightCounts = initTable[int, int](0)
for v in right:
    if not rightCounts.hasKey(v):
        rightCounts[v] = 0
    rightCounts[v] += 1

var part2Answer = 0
for value in left:
    if value in rightCounts:
        part2Answer += value * rightCounts[value]

echo "Part 2:", part2Answer
