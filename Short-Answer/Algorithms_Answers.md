#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This has a O(n) or linear time complexity since it grows in time as whatever is n grows.


b) This has a O(n log n) or Linearithmic time complexity since as the input increases in size, the runtime will increase slightly faster.


c) This has a O(n) or linear time complexity since within the function we have an if statement, which is constant and it's just returning another constant, and so the function will only grow as fast as n grows.

## Exercise II

# Well first of all, since it's never indicated where 'f' is, we need to find that sweet spot as soon as possible, without breaking too many eggs. 

`floors = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]` #Safest way to go to, in my opinion is splitting it in half and try then..
`half = [1,2,3,4,5,6,7]` #We drop the egg in floor `7`, if the egg breaks, we need to divide the half in half
`left_half = [1,2,3]` // `right_half = [4,5,6,7]` #We drop the egg in left_half, if it does not break, we need to access the right_half and split that in half
`right_half_half = [4,5]` #We drop the egg in right_half, if the egg did not break, we need to divide the right_half_half in half
`right_half_half_half = [6]` # We drop the egg and.. t did not break! And since in the first half it broke, it means that this will become f, so we can safely say that right_half_half_half is the sweet spot!

# This takes O(log n) since we can use a while loop and as long as the egg breaks, we can continue splitting in half until it doesn't.

