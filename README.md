## SameTree (To come back to binary tree code after a few lectures)
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value. 

![image](https://user-images.githubusercontent.com/36263575/65746396-ac5f1580-e0f6-11e9-822e-43a93ee1675a.png)

## SymmetricTree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric: 
![image](https://user-images.githubusercontent.com/36263575/65746748-85edaa00-e0f7-11e9-89bd-7f4cc7d5d608.png)

But the following [1,2,2,null,3,null,3] is not: 
![image](https://user-images.githubusercontent.com/36263575/65746789-a453a580-e0f7-11e9-8d3a-be75ba2c2edc.png) 

## BinaryTree 
Learning binary tree setup in python here: https://www.youtube.com/watch?v=YlgPi75hIBc

## MaxDepthTree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

![image](https://user-images.githubusercontent.com/36263575/65813008-fe6f6c00-e1c6-11e9-877d-90c2e02abc7f.png) 
return its depth = 3.

## StockTrading-1
Say you have an array for which the ith element is the price of a given stock on day i. 
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit. 
Note that you cannot sell a stock before you buy one. 

Example 1:

Input: [7,1,5,3,6,4] 
Output: 5 
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price. 

Example 2: 

Input: [7,6,4,3,1] 
Output: 0 
Explanation: In this case, no transaction is done, i.e. max profit = 0. 

## ValidPalindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

## SingleNumber
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

## Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack. 

pop() -- Removes the element on top of the stack. 

top() -- Get the top element. 

getMin() -- Retrieve the minimum element in the stack. 

Example: 

MinStack minStack = new MinStack(); 

minStack.push(-2); 

minStack.push(0); 

minStack.push(-3); 

minStack.getMin();   --> Returns -3. 

minStack.pop(); 

minStack.top();      --> Returns 0. 

minStack.getMin();   --> Returns -2. 

## TwoSum2
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note: 

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice. 

Example: 
 
Input: numbers = [2,7,11,15], target = 9 
Output: [1,2] 
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2. 
