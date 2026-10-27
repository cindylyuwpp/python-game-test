import pandas as pd

pd.set_option("display.width", 200)             # show all columns instead of "..."
pd.set_option("display.max_columns", None)

# ---------------------------------------------------------
# LOAD THE DATA
# ---------------------------------------------------------
df = pd.read_csv("ai_usage_log.csv")
df["date"] = pd.to_datetime(df["date"])          # treat the date column as real dates

print("=== First 5 rows ===")
print(df.head())
print(f"\nTotal generations logged: {len(df)}")

# ---------------------------------------------------------
# 1. WHICH MODELS DO I USE MOST?
# ---------------------------------------------------------
print("\n=== Uses per model ===")
print(df["model"].value_counts())

# ---------------------------------------------------------
# 2. IMAGES ONLY vs VIDEOS ONLY (filtering)
# ---------------------------------------------------------
images = df[df["media_type"] == "image"]
videos = df[df["media_type"] == "video"]
print(f"\nImages: {len(images)}   Videos: {len(videos)}")

print("\n=== Image models I used for brainstorming ===")
brainstorm = images[images["project_stage"] == "brainstorm"]
print(brainstorm["model"].value_counts())

# ---------------------------------------------------------
# 3. WHICH MODEL GIVES ME THE BEST RESULTS? (groupby + mean)
# ---------------------------------------------------------
print("\n=== Average rating per model (highest first) ===")
print(df.groupby("model")["rating"].mean().round(2).sort_values(ascending=False))

# ---------------------------------------------------------
# 4. HOW OFTEN DO I KEEP THE RESULT?
# ---------------------------------------------------------
df["kept_flag"] = df["kept"] == "yes"            # True/False column, so we can average it
print("\n=== Keep rate per model ===")
keep_rate = (df.groupby("model")["kept_flag"].mean() * 100).round(0)
print(keep_rate.sort_values(ascending=False).astype(int).astype(str) + "%")

# ---------------------------------------------------------
# 5. CREDITS: TOTAL SPENT AND COST PER KEPT RESULT
# ---------------------------------------------------------
summary = df.groupby("model").agg(
    uses=("model", "count"),
    total_credits=("credits_used", "sum"),
    kept=("kept_flag", "sum"),
)
summary["credits_per_kept"] = (summary["total_credits"] / summary["kept"]).round(1)
print("\n=== Credit summary ===")
print(summary.sort_values("total_credits", ascending=False))

# ---------------------------------------------------------
# 6. VIDEO HEAD-TO-HEAD: GEMINI OMNI FLASH vs RUNWAY GEN-4
# ---------------------------------------------------------
print("\n=== Video models compared ===")
print(videos.groupby("model")[["rating", "credits_used", "duration_sec"]].mean().round(1))

# ---------------------------------------------------------
# 7. USAGE OVER TIME (week by week)
# ---------------------------------------------------------
print("\n=== Generations per week ===")
weekly = df.groupby(df["date"].dt.to_period("W"))["model"].count()
print(weekly)
