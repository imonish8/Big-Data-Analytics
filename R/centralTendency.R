# Data
data <- c(10, 15, 20, 20, 25, 30, 35)

# Mean
mean_value <- mean(data)
print(paste("Mean:", mean_value))

# Median
median_value <- median(data)
print(paste("Median:", median_value))

# Mode (custom function, as R has no built-in mode function)
mode <- function(x) {
  uniq <- unique(x)
  uniq[which.max(tabulate(match(x, uniq)))]
}
mode_value <- mode(data)
print(paste("Mode:", mode_value))