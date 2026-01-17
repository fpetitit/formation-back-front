# Architectures Back-end & Front-end: Web, Mobile et IA

Présentation professionnelle réalisée avec **Reveal.js** couvrant les patterns d'architectures, clean code, microservices, et technologies modernes (Spring, Node.js, React, Flutter).

## 📋 Contenu de la présentation

**135 slides** organisés en 10 sections:

1. **Introduction** (10 slides)
   - Contexte et objectifs
   - Évolution des architectures
   - Panorama des technologies
   - Cas d'usage (assurance/santé)

2. **Patterns d'Architectures** (20 slides)
   - MVC, MVVM, CQRS
   - Event-Driven Architecture
   - Hexagonal Pattern
   - Dependency Injection, Repository, Strategy

3. **Clean Code et Clean Architecture** (15 slides)
   - Principes fondamentaux
   - 4 couches de Clean Architecture
   - Exemples et cas d'usage

4. **API et GraphQL** (15 slides)
   - REST vs GraphQL
   - Bonnes pratiques
   - Implémentation

5. **Microservices et Micro Frontends** (15 slides)
   - Architecture distribuée
   - Communication inter-services
   - Scalabilité

6. **SSR/SSG/SPA** (10 slides)
   - Server-Side Rendering
   - Static Site Generation
   - Single Page Applications

7. **Écosystème Java/Spring** (15 slides)
   - Spring Boot
   - Microservices avec Spring Cloud
   - Architecture distribuée

8. **Écosystème Node.js** (10 slides)
   - NestJS framework
   - Modules et services
   - API REST

9. **Frameworks Front-end** (15 slides)
   - React et Hooks
   - Gestion d'état
   - Composants réutilisables

10. **Technologies Mobiles** (10 slides)
    - React Native vs Flutter
    - Architecture mobile

**Bonus:**
- MCP et APIs pour l'IA (5 slides)
- Conclusion et récapitulatif (5 slides)

---

## 🚀 Installation

### Prérequis

- **Node.js** (v14+) et **npm**
- **Git** (optionnel, pour la gestion de version)
- Navigateur moderne (Chrome, Firefox, Safari, Edge)

### Étapes d'installation

1. **Cloner ou naviguer vers le projet:**
```bash
cd /home/francois/dev/code/formation
```

2. **Installer les dépendances:**
```bash
npm install
```

Ceci installe:
- `reveal.js` - Framework de présentation
- `highlight.js` - Coloration syntaxique pour les codes
- `marked` - Parseur Markdown

---

## 🎬 Lancer la présentation

### Option 1: Avec Python (simple)
```bash
python3 -m http.server 8000
```
Puis ouvrir http://localhost:8000 dans votre navigateur.

### Option 2: Avec un serveur Node.js
```bash
npx http-server
```

### Option 3: Avec Live Server (VS Code)
Installer l'extension "Live Server" dans VS Code, puis clic droit sur `index.html` → "Open with Live Server"

---

## 📖 Navigation dans la présentation

### Contrôles clavier

| Touche | Action |
|--------|--------|
| `→` / `←` | Slide suivant/précédent |
| `↓` / `↑` | Sous-section suivante/précédente |
| `Esc` | Vue d'ensemble (overview mode) |
| `F` | Plein écran |
| `S` | Notes du présentateur |
| `B` / `.` | Écran noir (pause) |
| `?` | Aide et raccourcis |

### Souris/Trackpad
- **Clic gauche:** Slide suivant
- **Clic droit:** Slide précédent
- **Molette:** Navigation verticale/horizontale

---

## 🎨 Personnalisation

### Modifier le thème

Le fichier `assets/css/theme.css` contient les styles personnalisés. Variables principales:

```css
:root {
  --primary-color: #1a1a1a;      /* Couleur primaire (textes) */
  --secondary-color: #ffffff;    /* Couleur secondaire */
  --accent-color: #0066cc;       /* Couleur d'accent (bleu) */
  --accent-dark: #004499;        /* Accent foncé */
  --text-color: #333333;         /* Couleur du texte */
  --light-bg: #f5f5f5;           /* Fond clair */
  --border-color: #dddddd;       /* Couleur des bordures */
}
```

Modifier ces variables pour changer les couleurs globalement.

### Ajouter des images

1. Placer les images dans `assets/images/`
2. Référencer dans les slides HTML:
```html
<img src="assets/images/mon-image.png" alt="Description">
```

### Modifier le contenu

Ouvrir `index.html` et chercher les sections `<!-- Slide X -->` pour éditer le contenu.

Chaque slide est un élément `<section>`:
```html
<section>
    <h2>Titre du slide</h2>
    <p>Contenu...</p>
</section>
```

### Ajouter des diagrammes Mermaid

Les diagrammes utilisent **Mermaid.js** (CDN intégré). Exemple:

```html
<div class="mermaid">
    graph LR
        A["Backend"] -->|API| B["Frontend"]
</div>
```

Syntaxe Mermaid: https://mermaid.js.org/

---

## 📁 Structure du projet

```
formation/
├── index.html                  # Fichier principal de la présentation
├── package.json               # Dépendances npm
├── README.md                  # Ce fichier
├── .gitignore                 # Fichiers à ignorer (git)
│
├── assets/
│   ├── css/
│   │   └── theme.css         # Thème personnalisé minimaliste
│   ├── images/               # Images de la présentation
│   ├── videos/               # Vidéos (si besoin)
│   └── data/                 # Données statiques (JSON, CSV)
│
├── slides/                    # Dossier pour slides additionnels (optionnel)
│
└── node_modules/             # Dépendances (généré, dans .gitignore)
```

---

## 🛠 Configuration Reveal.js

Les options principales dans `index.html`:

```javascript
Reveal.initialize({
    hash: true,                 // URL hashes pour la navigation
    margin: 0.1,               // Marge autour des slides
    center: false,             // Contenu aligné à gauche
    transition: 'slide',       // Type de transition
    transitionSpeed: 'default', // Vitesse des transitions
    slideNumber: true,         // Afficher le numéro du slide
    overview: true,            // Mode overview (Esc)
    keyboard: true,            // Navigation au clavier
    touch: true,              // Navigation tactile
    help: true,               // Afficher l'aide (?)
    width: 1400,              // Largeur de la présentation
    height: 900,              // Hauteur de la présentation
    minScale: 0.2,            // Zoom minimum
    maxScale: 2.0             // Zoom maximum
});
```

Pour modifier, éditer directement dans `index.html` à la fin du fichier.

---

## 🌐 Déployer la présentation

### Sur GitHub Pages

1. Créer un repo GitHub `mon-formation`
2. Pousser le code:
```bash
git init
git add .
git commit -m "Initial commit: presentation revealjs"
git branch -M main
git remote add origin https://github.com/username/mon-formation.git
git push -u origin main
```

3. Activer GitHub Pages:
   - Settings → Pages
   - Source: `main` branch
   - Sauvegarder

4. Accéder à: `https://username.github.io/mon-formation/`

### Sur Netlify

1. Connecter le repo GitHub
2. Build command: (laisser vide)
3. Publish directory: `.` (racine)
4. Deploy!

### Sur un serveur personnel

```bash
# Copier le dossier sur le serveur
scp -r formation/ user@server:/var/www/html/

# Accéder à: http://server-ip/formation/
```

---

## 📝 Notes pour les présentateurs

- Appuyer sur `S` pour voir les notes du présentateur (à ajouter dans `<aside class="notes">`)
- Utiliser le mode overview (`Esc`) pour naviguer rapidement
- Préparer le plein écran (`F`) avant de présenter
- Tester la présentation sur le dispositif final avant la présentation

Exemple d'ajout de notes:
```html
<section>
    <h2>Mon slide</h2>
    <aside class="notes">
        Parler de X, mentionner Y, insister sur Z
    </aside>
</section>
```

---

## 🐛 Dépannage

### Les diagrammes Mermaid ne s'affichent pas
- Vérifier la connexion Internet (Mermaid est en CDN)
- Actualiser la page (F5)
- Ouvrir la console du navigateur (F12) pour voir les erreurs

### Les styles ne s'appliquent pas
- Vérifier que `assets/css/theme.css` existe
- Nettoyer le cache du navigateur (Ctrl+Shift+Delete)
- Vérifier les chemins d'accès dans `index.html`

### Problèmes de navigation
- Vérifier que Reveal.js est bien chargé: ouvrir la console (F12) et chercher les erreurs
- Tester avec un autre navigateur
- Vérifier les versions de Node.js et npm: `node --version` et `npm --version`

---

## 📚 Ressources

- **Reveal.js:** https://revealjs.com/
- **Mermaid Diagrams:** https://mermaid.js.org/
- **Highlight.js:** https://highlightjs.org/
- **Documentation Reveal.js:** https://revealjs.com/api/

---

## 📄 Licence

Libre d'utilisation et de modification.

---

## 👤 Auteur

Formation continue - 2026

**Durée:** 6 heures  
**Public:** Développeurs, Architectes, Chefs de projet  
**Technologies couvertes:** Java/Spring, Node.js/NestJS, React, Vue, Angular, Next.js, React Native, Flutter, Microservices, GraphQL, et bien plus!

---

## 📞 Support

Pour les questions ou améliorations, consulter la documentation de Reveal.js ou les exemples dans le code HTML.

Bon apprentissage! 🚀
