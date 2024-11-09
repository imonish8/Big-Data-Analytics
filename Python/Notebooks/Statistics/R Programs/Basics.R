myVector <- c(1,22.22, 'Hello', 1000)
noString = c(1,2,3,44,33.2)
noFloat <- c(1,2,3,4,5)
print(noString)
print(myVector)
print(noFloat)

add <- function(x, y) {
    return(x + y)
}

res <- add(5,5)
print(f"addition res {res}")