# Example R script with a plot
x <- 1:10
y <- x^2
png("plot_example.png") # Save plot as an image file
plot(x, y, main = "Example Plot", xlab = "X", ylab = "Y^2")
dev.off() # Close the graphic device