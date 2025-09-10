cat("\n\nTitel: Practical Exercise 02 - Tropical Crop Production 2025\n")
cat("Author: Lucas Daniel Paz Zuleta, TZS159\n")
cat("Date:", format(Sys.Date(), "%d-%m-%Y"), "\n\n")

# --- Paths ---
data_path <- file.path("/Users/bruger/Desktop/Folders/KU/Master/year_2/blok_01/TCP/tcp_notes/tcp_project_files/R/data/PE2_germination_data_exercise.csv") # Update the path to the correct file in your data folder
fig_dir   <- file.path("/Users/bruger/Desktop/Folders/KU/Master/year_2/blok_01/TCP/tcp_notes/tcp_project_files/R/figures/PE2") # Leave this as is, unless you want to change the figure directory

# Check if the figures directory exists, create it if not
if (!dir.exists(fig_dir)) dir.create(fig_dir, recursive = TRUE)

# Check if the data file exists
if (!file.exists(data_path)) {
    stop("The data file does not exist at the specified path: ", data_path)
}

# This code is used for the lecture and the exercise.

# For the exercise you might need to change the number of parameters and 
#the best model to use for plotting. Look for the "CLUES"
# Remember to format the exercise data to fit the code 
# (column names, format etc.)


# --- Package & Git Repo installation ---
# If the following has not been installed yet, please ensure to install it 
# before running the code. Otherwise, you can skip this part.

# install.packages("dplyr")
# install.packages("ggplot2")
# install.packages("devtools")
# install.packages("magic")
# library(devtools)
# install_github("DoseResponse/drcData", dependencies = TRUE, force =TRUE)
# install_github("DoseResponse/drc", dependencies = TRUE, force =TRUE)
# install_github("DoseResponse/bmd", dependencies = TRUE, force =TRUE)


# --- Load libraries ---
library(drc)
library(bmd)
library(dplyr)
library(ggplot2)
library(magic)


# --- Reading the dataset from R/data/ --- 

m <- read.csv(data_path)   # European CSVs → use read.csv2()

#  --- Initial exploration of the data --- 
cat("\nFirst rows of the data:\n")
print(head(m)) # First rows of the data

cat("\nLast rows of the data:\n")
print(tail(m)) # Last rows of the data

cat("\nStructure of the data:\n")
str(m) # Structure of the data

# --- Exploratory Data Analysis (EDA) - Cumulative Observations ---
# This step can be skipped if the data is already in cumulative format (like it is now)

# m_cumu <- m %>%
#   dplyr::group_by(time_days, treatment_id, treatment_value_gpel_l) %>%
#   dplyr::mutate(cumulative_observations = cumsum(obs_germination))
#
# cat("\n-- HEAD (cumulative) --\n")
# print(head(m_cumu))
#
# cat("\n-- TAIL (cumulative) --\n")
# print(tail(m_cumu))

# --- Exploratory Data Analysis (EDA) - Plots ---
# Plot cumulative observations over time for each treatment
ggplot(m, aes(x = time_days, y = obs_germination, color = as.factor(treatment_value_gpel_l))) +
  geom_point() +
  geom_line() +
  labs(title = "Germination Observations Over Time by Treatment",
       x = "Time (days)",
       y = "Germination Observations",
       color = "Treatment (g pel l)") +
  theme_classic() +
  theme(plot.title = element_text(hjust = 0.5)) # Center the title

# Save the plot
ggsave(filename = file.path(fig_dir, "germination_observations_over_time.png"), width = 8, height = 6)
cat("\nGermination observations over time plot saved to figures directory.\n")

# If the plot looks good, and the data is in cumulative format, we can proceed to the next step.

# --- Dose-Response Modelling ---
# ?drm - for help on the drm function

# If you want to see all the available models, use:
# getMeanFunctions()

# In this case we will choose LL.3() - 3 parameter log-logistic model (obs_germination, time_days, and treatment_ID)

# Start by ensuring the column names:
colnames(m) # Check column names in the dataset

# Ensure treatment_id is a factor
m$treatment_id <- as.factor(m$treatment_id)

# Fit the model
model_LL <- drm(
  obs_germination ~ time_days,          # response ~ predictor
  fct       = LL.3(),                   # model function (try LL.3(), LL.4(), LL.5())
  data      = m,                        # dataset
  curveid   = treatment_id,             # grouping variable for curves
  separate  = TRUE,                     # fit each treatment independently
  type      = "continuous"              # type of data
)

# If no errors, proceed to summary
# Model summary
cat("\nModel Summary:\n")
print(summary(model_LL))

# Plot the model fit
cat("\nPlotting the dose-response model fit...\n")
plot(model_LL, log = "", col = 1:6, lwd = 2, xlab = "Time (days)", ylab = "Germination Observations")
title("Dose-Response Model Fit (LL.3)")
legend("topleft", legend = levels(m$treatment_id), col = 1:6, lwd = 2)
# Save the plot
dev.copy(png, filename = file.path(fig_dir, "dose_response_model_fit_LL3.png"), width = 800, height = 600)
dev.off()
cat("\nDose-response model fit plot saved to figures directory.\n")

# --- Model Comparison ---
# Fit alternative models for comparison
model_LL4 <- drm(
  obs_germination ~ time_days,
  fct       = LL.4(),
  data      = m,
  curveid   = treatment_id,
  separate  = TRUE,
  type      = "continuous"
)
model_W1 <- drm(
  obs_germination ~ time_days,
  fct       = W1.4(),
  data      = m,
  curveid   = treatment_id,
  separate  = TRUE,
  type      = "continuous"
)
model_W2 <- drm(
  obs_germination ~ time_days,
  fct       = W2.4(),
  data      = m,
  curveid   = treatment_id,
  separate  = TRUE,
  type      = "continuous"
)

# --- Compare models using AIC ---
# Extract AIC values for each treatment and model
aic_df_LL <- data.frame(
  Treatment = names(model_LL$objList),
  AIC_LL    = sapply(model_LL$objList, function(f) tryCatch(AIC(f), error=function(e) NA_real_)),
  row.names = NULL
)

aic_df_W1 <- data.frame(
  Treatment = names(model_W1$objList),
  AIC_W1    = sapply(model_W1$objList, function(f) tryCatch(AIC(f), error=function(e) NA_real_)),
  row.names = NULL
)

aic_df_W2 <- data.frame(
  Treatment = names(model_W2$objList),
  AIC_W2    = sapply(model_W2$objList, function(f) tryCatch(AIC(f), error=function(e) NA_real_)),
  row.names = NULL
)

# Merge and pick best per treatment
aic_all <- Reduce(function(x, y) merge(x, y, by = "Treatment", all = TRUE),
                  list(aic_df_LL, aic_df_W1, aic_df_W2))

# Winner column
cols <- c("AIC_LL", "AIC_W1", "AIC_W2")
aic_all$Best <- cols[max.col(-as.matrix(aic_all[ , cols, drop = FALSE]))]

print(aic_all)

# Choose the lowest AIC model for further analysis
    # Overall best model across treatments = lowest total AIC
totals <- colSums(aic_all[, cols], na.rm = TRUE)
cat("\n\nOverall best model by total AIC:", overall_best, "\n")   
print(totals)
overall_best <- names(which.min(totals))

cat("\n\nOverall best model by total AIC:\n", overall_best, "\n")

# --- Treatment Comparisons ---
# Using the best model (e.g., model_LL) for treatment comparisons
plot(
    best_model, 
    log     = "", 
    col     = 1:6, 
    lwd     = 2, 
    xlab    = "Time (days)", 
    ylab    = "Germination Observations",
    xlim    = range(m$time_days, na.rm = TRUE),
    ylim    = range(m$obs_germination, na.rm = TRUE)
    )
title(paste("Best Dose-Response Model Fit (", overall_best, ")", sep = ""))
legend(
    "topleft", 
    legend = levels(m$treatment_id), 
    col = 1:6, 
    lwd = 2
    )

# Save the plot
dev.copy(
    png, 
    filename = file.path(fig_dir, paste0("best_dose_response_model_fit_", 
    overall_best, ".png")), 
    width = 800, 
    height = 600
    )
dev.off()
cat("\nBest dose-response model fit plot saved to figures directory.\n")

# Using the main solution
qplotDrc(best_model, 
            col=TRUE,
            xlab="Time (days)",
            ylab="Germination Observations",
            labs(col="Treatment (g pel l)")) +
    theme_classic() +
    theme(plot.title = element_text(hjust = 0.5)) # Center the title
# Save the plot
ggsave(filename = file.path(fig_dir, paste0("qplot_best_dose_response_model_fit_", overall_best, ".png")), width = 8, height = 6)
cat("\nQplot of best dose-response model fit saved to figures directory.\n")

