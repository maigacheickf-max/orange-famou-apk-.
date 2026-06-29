"""
Applique l'icône resources/icon.png à toutes les résolutions Android
nécessaires (mdpi à xxxhdpi), pour que l'app ait une vraie icône au lieu
de l'icône par défaut de Capacitor.
"""
import os

try:
    from PIL import Image
except ImportError:
    os.system("pip install pillow --quiet --break-system-packages")
    from PIL import Image

src = Image.open("resources/icon.png").convert("RGB")

sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}

base = "android/app/src/main/res"
for folder, size in sizes.items():
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)
    resized = src.resize((size, size), Image.LANCZOS)
    resized.save(os.path.join(path, "ic_launcher.png"))
    resized.save(os.path.join(path, "ic_launcher_round.png"))
    resized.save(os.path.join(path, "ic_launcher_foreground.png"))

print("Icônes appliquées avec succès sur toutes les résolutions.")
