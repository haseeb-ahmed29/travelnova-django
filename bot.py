def run_job(name="daily_sync"):
    return {"job": name, "status": "queued"}

if __name__ == "__main__": print(run_job())
