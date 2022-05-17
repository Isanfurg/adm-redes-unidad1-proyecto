from locust import HttpUser, TaskSet, task

   
class WebsiteUser(HttpUser):
    @task(3)
    def ver_home(self):
        self.client.get("/")
    @task(2)
    def ver_categoria(self):
        self.client.get("/index.php?id_category=3&controller=category")
    @task(4)
    def ver_categoria_gamer(self):
        self.client.get("/index.php?id_category=5&controller=category")
    @task(1)
    def ver_silla(self):
        self.client.get("/index.php?id_product=22&rewrite=silla-gamer-profesional-e-blue-cobra&controller=product")
        
    min_wait = 5000
    max_wait = 9000
