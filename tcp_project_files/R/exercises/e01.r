cat("Titel: Practical Exercise 02 - Tropical Crop Production 2025\n")
cat("Author: Lucas Daniel Paz Zuleta, TZS159\n")
cat("Date:", format(Sys.Date(), "%d-%m-%Y"), "\n\n")

# --- Paths ---
data_path <- "R/data/PE2_germination_data_exercise.csv" # insert the necesary path here
fig_dir   <- "R/figures" # leave this be, unless you want to change the figure directory

if (!dir.exists(fig_dir)) dir.create(fig_dir)

# This code is used for the lecture and the exercise.

# For the exercise you might need to change the number of parameters and the best model to use for plotting. Look for the "CLUES"
# Remember to format the exercise data to fit the code (column names, format etc.)


# --- Package & Git Repo installation ---
# If the following has not been installed yet, please ensure to install it before running the code. Otherwise, you can skip this part.

# install.packages("dplyr")
# install.packages("ggplot2")
# install.packages("devtools")
# library(devtools)
# install_github("DoseResponse/drcData", dependencies = TRUE, force =TRUE)
# install_github("DoseResponse/drc", dependencies = TRUE, force =TRUE)
# install_github("DoseResponse/bmd", dependencies = TRUE, force =TRUE)


# --- Load libraries ---
library(drc)
library(bmd)
library(dplyr)
library(ggplot2)


# Reading the dataset from R/data/

m <- read.csv("R/data/PE2_germination_data_exercise.csv")   # European CSVs → use read.csv2()

head(m)
tail(m)



