# Orange Famou Burkina — Version Android (APK)

Ce dossier transforme l'application "Orange Famou" (HTML) en une vraie
application Android, grâce à **Capacitor**.

Le contenu de l'app est dans `www/index.html` (déjà inclus, avec les
animations et le drapeau du Burkina Faso). Si tu modifies ce fichier,
il suffit de relancer le build (étape 4) pour obtenir un nouvel APK.

---

## Obtenir l'APK via GitHub Actions (gratuit, automatique)

GitHub Actions installe Android, compile l'app et te donne un fichier
`.apk` prêt à installer — tu n'as rien à installer sur ton ordinateur.

### Étape 1 — Créer un compte GitHub (si tu n'en as pas)
Va sur https://github.com et crée un compte gratuit.

### Étape 2 — Créer un nouveau dépôt (repository)
1. Va sur https://github.com/new
2. Donne-lui un nom, par exemple `orange-famou-apk`
3. Laisse-le en **Public** ou **Private**
4. Ne coche aucune case (pas de README, pas de .gitignore — déjà inclus)
5. Clique sur **"Create repository"**

### Étape 3 — Envoyer ce dossier sur GitHub
Ouvre un terminal **dans ce dossier** (`orange-famou-apk`) et tape :

```bash
git init
git add .
git commit -m "Premier envoi de l'app Android"
git branch -M main
git remote add origin https://github.com/TON-COMPTE/orange-famou-apk.git
git push -u origin main
```

(Remplace `TON-COMPTE` et `orange-famou-apk` par tes propres valeurs.)

### Étape 4 — Laisser GitHub construire l'APK
1. Va sur la page de ton dépôt GitHub
2. Clique sur l'onglet **"Actions"**
3. Une exécution **"Build Orange Famou Burkina (APK Android)"** démarre
4. Attends 4 à 8 minutes (le premier build Android est un peu plus long)

### Étape 5 — Télécharger l'APK
1. Clique sur l'exécution terminée (✅ vert)
2. En bas de page, section **"Artifacts"** → **OrangeFamouBurkina-Android-APK**
3. Télécharge, dézippe : tu obtiens `app-debug.apk`

### Étape 6 — Installer l'APK sur un téléphone Android
1. Transfère `app-debug.apk` sur le téléphone (câble USB, WhatsApp, Drive...)
2. Ouvre le fichier depuis le téléphone
3. Android demandera d'autoriser **"Installer des apps inconnues"** pour
   l'application utilisée pour ouvrir le fichier (ex : Fichiers, Drive) —
   c'est normal, c'est juste parce que l'app ne vient pas du Play Store
4. Accepte, installe, et l'app apparaît sur l'écran d'accueil 🎉

---

## Relancer un build après une modification

```bash
git add .
git commit -m "Mise à jour"
git push
```

GitHub Actions régénère automatiquement un nouvel APK.

---

## Important à savoir

- L'APK généré est une version **debug**, parfaite pour installer et tester
  directement sur un téléphone ou à partager. Elle n'est pas signée pour le
  Play Store.
- Si un jour tu veux **publier l'app sur le Google Play Store**, il faudra
  une version "release" signée avec une clé — dis-le moi et je préparerai
  cette étape en plus (elle demande de créer et garder en sécurité un
  fichier de signature).

---

## Structure du projet

```
orange-famou-apk/
├── www/
│   └── index.html              ← le contenu de l'app
├── resources/
│   └── icon.png                 ← icône de l'app (1024×1024)
├── capacitor.config.js          ← configuration Capacitor (nom, id de l'app)
├── package.json
├── scripts/
│   └── apply_icon.py            ← applique l'icône à toutes les résolutions
└── .github/workflows/
    └── build-android.yml         ← instructions pour GitHub Actions
```

Note : le dossier `android/` n'existe pas dans ce zip — GitHub Actions le
génère automatiquement à chaque build à partir de `capacitor.config.js`.
C'est normal et volontaire (ce dossier est volumineux et regénérable).
