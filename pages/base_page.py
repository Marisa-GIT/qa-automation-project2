class BasePage:
    def __init__(self, page):
        self.page = page
    
    def navigate(self, url):
        print(f"\nNavigating to: {url}")
        try:
            self.page.goto(url, wait_until="load")
        except Exception as e:
            print(f"Error while navigating: {e}")
            raise