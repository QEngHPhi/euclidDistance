import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 2D uzaydaki noktaları içeren bir liste
points = [(1, 2), (4, 6), (7, 8), (2, 1)]

# Mesafeleri saklamak için bir liste
distances = []

# Nokta çiftleri arasındaki mesafeleri hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Her çifti bir kez hesaplarsınız
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonuçları yazdırma
print("Noktalar:", points)
print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)
