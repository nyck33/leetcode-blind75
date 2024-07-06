-- Define a custom linked list data type
data Node a = Node a (Node a) | End deriving (Eq, Show)

-- Function to move one step in the list
step :: Node a -> Node a
step (Node _ next) = next
step End = End

-- Function to move two steps in the list
doubleStep :: Node a -> Node a
doubleStep (Node _ (Node _ next)) = next
doubleStep _ = End

-- Floyd's Tortoise and Hare algorithm to detect cycles
hasCycle :: Eq a => Node a -> Bool
hasCycle list = hasCycle' list list
  where
    hasCycle' :: Eq a => Node a -> Node a -> Bool
    hasCycle' tortoise hare
      | hare == End || step hare == End = False -- No cycle if hare reaches the end
      | tortoise == hare = True -- Cycle detected
      | otherwise = hasCycle' (step tortoise) (doubleStep hare)

-- Create a function to build a cyclic list for testing
buildCyclicList :: Int -> Node Int
buildCyclicList n = let node = Node n node in node

-- Create a function to build a non-cyclic list for testing
buildNonCyclicList :: [Int] -> Node Int
buildNonCyclicList [] = End
buildNonCyclicList (x:xs) = Node x (buildNonCyclicList xs)

-- Test the hasCycle function
main :: IO ()
main = do
    print $ hasCycle (buildCyclicList 1) -- Should print True
    print $ hasCycle (buildNonCyclicList [1, 2, 3, 4, 5]) -- Should print False