---
theme: unicorn
title: Architectures Back-end
subtitle: Web, Mobile et IA
date: 2026-01-17
layout: cover
download: true
logoHeader: 'https://s2.qwant.com/thumbr/474x248/6/1/af7e04834307a6e98c63ca1e9e06f6a30e6a1da544329d0879a35f520e5b4a/OIP.-GR5tY0qTW9kY_XXgyW3EwHaD4.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.-GR5tY0qTW9kY_XXgyW3EwHaD4%3Fcb%3Ddefcachec2%26pid%3DApi&q=0&b=1&p=0&a=0'
---

# Architectures Back-end

Back-ends et API pour le Web, le Mobile et l'IA

---
layout: table-contents
gradientColors: ['#8EC5FC', '#E0C3FC']
---

# 📋 Sommaire

- 🔧 Fondamentaux & Introduction
- 🏗️ Patterns d'Architecture
- 🚀 Architectures Avancées
- 🎨 Écosystèmes Technologiques
- ✨ Développement Propre
- 🌐 APIs & Communication
- � Messaging Asynchrone
- 🔒 Sécurité Avancée
- ⚡ Benchmarks de Performance
- 🔢 Nombres Clés
- 🤖 Intégration IA

---
src: ./pages/historique-architectures.md
---

---
src: ./pages/ecosystemes-backend.md
---

## Évolution des architectures

```mermaid
graph LR
                            A["<b>Monolithique</b><br/>(2000s)"] -->|Complexité croissante| B["<b>Microservices</b><br/>(2010s)"]
                            B -->|Optimisation| C["<b>Serverless</b><br/>(2020s)"]
                            
                            style A fill:#e8f4f8
                            style B fill:#fff4e8
                            style C fill:#e8f8e8
```

| Architecture | Avantages | Inconvénients |
| --- | --- | --- |
| Monolithe | Simple, facile à déployer | Difficile à scaler, couplage fort |
| Microservices | Scalable, indépendant | Complexité opérationnelle |
| Serverless | Pas de gestion infra | Coûts imprévisibles, latence |


---

## Défis de l'architecture moderne

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 20px;">
<div style="display: grid; grid-template-columns: 1fr; gap: 30px; ">

#### 🚀 Performance


- Latence réduite
- Caching efficace
- Scalabilité

#### 🔒 Sécurité


- OAuth2, JWT
- HTTPS, TLS
- Validation des données

</div>
<div style="display: grid; grid-template-columns: 1fr; gap: 30px; ">

#### 📊 Scalabilité


- Horizontal scaling
- Load balancing
- Caching distribué

#### 🔄 Maintenabilité

- Documentation
- Tests automatisés
- CI/CD pipeline
</div>
</div>

---
src: ./pages/patterns.md
---
---
src: ./pages/transactions.md
---
---
src: ./pages/microservices.md
---

---
src: ./pages/async-messaging.md
---

---
src: ./pages/serverless.md
---
---
src: ./pages/cache.md
---

# 🗃️ Database Sharding et Partitioning

---

## Définitions

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>

### Sharding Horizontal

```mermaid
graph TB
    A["📊 Données"] --> B["🔪 Partitionnement"]
    B --> C["Shard 1"]
    B --> D["Shard 2"]
    B --> E["Shard N"]

    style A fill:#e8f4ff
    style B fill:#ff6b6b
    style C fill:#fff9e8
    style D fill:#ffe8f4
    style E fill:#e8ffe8
```

</div>
<div>

### Partitioning Vertical

```mermaid
graph TB
    A["📊 Table"] --> B["🔪 Séparation"]
    B --> C["Colonnes A-B"]
    B --> D["Colonnes C-D"]
    B --> E["Colonnes E-F"]

    style A fill:#e8f4ff
    style B fill:#ff6b6b
    style C fill:#fff9e8
    style D fill:#ffe8f4
    style E fill:#e8ffe8
```
</div>
</div>

---

## Stratégies de Sharding

### 1. Key-Based Sharding

```mermaid
graph LR
    A["🔑 Clé"] -->|Hash| B["📊 Shard"]
    B --> C["🗄️ Stockage"]

    style A fill:#e8f4ff
    style B fill:#fff9e8
    style C fill:#ffe8f4
```

### 2. Range-Based Sharding

```mermaid
graph LR
    A["📏 Plage de valeurs"] --> B["📊 Shard 1"]
    C["📏 Plage suivante"] --> D["📊 Shard 2"]

    style A fill:#e8f4ff
    style B fill:#fff9e8
    style C fill:#ffe8f4
    style D fill:#e8ffe8
```

---

## Implémentation Pratique

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>

### PostgreSQL avec Citus

```mermaid
graph LR
    A["📱 Application"] --> B["🔄 Coordinateur"]
    B --> C["🗄️ Worker 1"]
    B --> D["🗄️ Worker 2"]
    B --> E["🗄️ Worker N"]

    style A fill:#e8f4ff
    style B fill:#ffd700
    style C fill:#fff9e8
    style D fill:#ffe8f4
    style E fill:#e8ffe8
```
</div>
<div>

### MongoDB Sharding

```mermaid
graph LR
    A["📱 Client"] --> B["🎯 Mongos"]
    B --> C["🗄️ Config Servers"]
    B --> D["📊 Shard 1"]
    B --> E["📊 Shard 2"]

    style A fill:#e8f4ff
    style B fill:#ffd700
    style C fill:#fff9e8
    style D fill:#ffe8f4
    style E fill:#e8ffe8
```

</div>
</div>
---

---
src: ./pages/performance-benchmarks.md
---

---
src: ./pages/key-metrics.md
---
src: ./pages/ddd.md
---

---
src: ./pages/clean-code.md
---

---
src: ./pages/api.md
---

---
src: ./pages/security-advanced.md
---

---
src: ./pages/ia-mcp.md
---

---

## Ressources & Références

#### Ouvrages de Référence

**Clean Code** - Robert C. Martin
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

**Clean Architecture** - Robert C. Martin
> "A software architect is a programmer who has stopped programming and has started thinking about programs."

**Design Patterns** - Gang of Four (Gamma, Helm, Johnson, Vlissides)
> "The purpose of design patterns is to give a name and a context to design problems and their solutions."

**Building Microservices** - Sam Newman
> "Microservices are small, autonomous services that work together. The microservice architectural style is an approach to developing a single application as a suite of small services."

**Domain-Driven Design** - Eric Evans
> "When you model using only the semantics that the business expert cares about, you get a model that the business expert understands."

**The Pragmatic Programmer** - Hunt & Thomas
> "Leave the campground cleaner than you found it. Leave the code better than you found it."

**Refactoring: Improving the Design of Existing Code** - Martin Fowler
> "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."

---

## Questions & Discussion

### Qu'avez-vous envie de discuter?

✋ Levez la main pour poser vos questions
💬 Débat sur technologies, architecture...
🤔 Cas d'usage spécifiques à votre contexte


Pas de question bête - cette partie est pour VOUS

---

## Merci! 🙏

---
