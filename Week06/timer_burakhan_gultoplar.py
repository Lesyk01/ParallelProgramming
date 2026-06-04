import time

class SureOlcer:

    def __init__(self):
        self.baslangic = None
        self.bitis = None
        self.gecen_sure = None

    def __enter__(self):
        self.baslangic = time.perf_counter()  
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.bitis = time.perf_counter()
        self.gecen_sure = self.bitis - self.baslangic
        print(f"[Zamanlayıcı] İşlem süresi: {self.gecen_sure:.5f} saniye")
