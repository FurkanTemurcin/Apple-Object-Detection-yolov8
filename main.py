from ultralytics import YOLO
import os
import yaml

def main():
    # 1. Senin verdiğin ana klasör yolu
    base_path = r"C:\Users\FURKAN\OneDrive\Masaüstü\ElmaProjesi"
    
    # data.yaml dosyasının yeri
    yaml_file = os.path.join(base_path, 'data.yaml')

    print(f"Çalışma dizini: {base_path}")
    
    # 2. data.yaml dosyasını senin yoluna göre otomatik düzeltelim
    # (Böylece yol hatası almazsın)
    try:
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
        
        # Yolları tam yol (Absolute Path) olarak güncelliyoruz
        data['path'] = base_path
        data['train'] = os.path.join(base_path, 'train', 'images')
        data['val'] = os.path.join(base_path, 'valid', 'images')
        data['test'] = os.path.join(base_path, 'test', 'images')
        
        # Düzeltilmiş dosyayı kaydediyoruz
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f)
        print("data.yaml dosyası senin klasör yoluna göre güncellendi!")
        
    except Exception as e:
        print(f"UYARI: data.yaml güncellenirken hata oldu ama eğitime devam ediliyor. Hata: {e}")

    # 3. Modeli Yükle
    model = YOLO('yolov8n.pt')  

    # 4. Eğitimi Başlat
    print("Eğitim başlıyor, lütfen bekleyin...")
    results = model.train(
        data=yaml_file, 
        epochs=20, 
        imgsz=640,
        name='elma_sonuc'
    )

if __name__ == '__main__':
    main()