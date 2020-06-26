# Mock Interview: Mountain Array.

## Objective.

There is a list of some arrays of ingtegers. Please, build a code that validates if each array on the list is or not a mountain array.

```python
Array_list = [[0,2,3,4,5,2,1,0], [1,2,3,1], [1,2,3,4,5], [5,4,3,2,1], [1,2,3,4,4,4,5,0], [1,2,3,4,5,4,3,2,1], [2,1],[0,3,2,1], [3,5,5]]
```
## Background.

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

```python
len(A) >= 3
```
There exists some` i` with `0 < i <(len(A) - 1)` such that:
`A[0] < A[1] < ... A[i-1] < A[i]`
`A[i] > A[i+1] > ... > A[A.length - 1]`

## Examples

- **Example 1:**

`Input: [2,1]
Output: False`

- **Example 2:**

`Input: [3,5,5]
Output: false`

- **Example 3:**

`Input: [0,3,2,1]
Output: true`

## Notes.

- This mock interview was proposed by Pablo Trinidad (@pablotrinidad) conducted by Nicolas Arias (@Narias1999) on june 25th, 2020. Please, follow them on GithHub and their Social Networks.

- The backgrund and examples were taken from LeetCode site. There is the source link  https://leetcode.com/articles/valid-mountain-array/
