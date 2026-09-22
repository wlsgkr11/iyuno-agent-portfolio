import json
import matplotlib.pyplot as plt

with open("evaluation/metrics.json", "r", encoding="utf-8") as f:
    metrics = json.load(f)

recall = metrics["retrieval"]["recall_at_3"]
latency = metrics["latency"]["average_seconds"]

fig = plt.figure()
plt.bar(["Recall@3"], [recall])
plt.ylim(0, 1.1)
plt.ylabel("Score")
plt.title("RAG Retrieval Performance")
plt.text(0, recall + 0.03, f"{recall:.2f}", ha="center")
plt.tight_layout()
plt.savefig("evaluation/recall_at_3.png", dpi=150)
plt.close()

fig = plt.figure()
plt.bar(["Average Latency"], [latency])
plt.ylabel("Seconds")
plt.title("Average Retrieval Latency")
plt.text(0, latency + 0.01, f"{latency:.3f}s", ha="center")
plt.tight_layout()
plt.savefig("evaluation/latency.png", dpi=150)
plt.close()

print("Evaluation graphs created.")
print("evaluation/recall_at_3.png")
print("evaluation/latency.png")
