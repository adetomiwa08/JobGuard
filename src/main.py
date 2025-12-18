# main.py
from src.fetch_jobs import fetch_jobs
from src.analyze import analyze_job
from src.save import save_report

def main():
    jobs = fetch_jobs()
    if not jobs:
        print("No jobs found. Exiting.")
        return

    results = []
    for job in jobs:
        result = analyze_job(job)
        results.append(result)

        # Real-time console alert
        if result["status"] == "Unsafe":
            print(f"\nWARNING: Suspicious job detected -> {result['title']}")
            for alert in result["alerts"]:
                print(f" - {alert}")
        else:
            print(f"Safe job -> {result['title']}")

    save_report(results)
    print("\nJobGuard scan completed!")

if __name__ == "__main__":
    main()
