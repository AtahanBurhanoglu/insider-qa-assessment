from locust import HttpUser, task, between

class N11SearchUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://www.n11.com"
    
    # Bot korumasını (403) aşmak için gerçek tarayıcı kimliği
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"'
    }

    @task(1)
    def load_homepage(self):
        with self.client.get("/", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Homepage load failed with status: {response.status_code}")

    @task(2)
    def search_product(self):
        search_term = "bilgisayar"
        with self.client.get(f"/arama?q={search_term}", headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Search failed with status: {response.status_code}")
