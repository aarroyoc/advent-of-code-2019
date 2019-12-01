main :: IO ()
main = do
    file <- readFile "input"
    let numbers = map (read::String->Int) (lines file)
    let fuelNumbers = map fuel2 numbers
    putStrLn (show $ sum fuelNumbers)

fuel :: Int -> Int
fuel x = 
    let
        y = x `div` 3
        z = y-2
    in
        if z > 0 then z else 0

fuel2 :: Int -> Int
fuel2 x =
    let
        y = fuel x
    in
        if y > 0 then
            fuel2 y + y
        else
            y