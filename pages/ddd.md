
# 🎯 Domain-Driven Design

---

## Strategic vs Tactical DDD

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 20px;">
<div>

### Niveaux de DDD

```mermaid
graph TD
    A["🎯 Strategic DDD"] --> B["🔧 Tactical DDD"]
    B --> C["📦 Implementation"]

    style A fill:#ffd700
    style B fill:#ffe8f4
    style C fill:#fff9e8
```

</div>
<div>

### Strategic DDD

- **Bounded Contexts**: Frontières claires
- **Context Mapping**: Relations entre contextes
- **Ubiquitous Language**: Langage commun

### Tactical DDD

- **Aggregates**: Cohérence transactionnelle
- **Domain Events**: Communication asynchrone
- **Entities vs Value Objects**: Modélisation fine

</div>
</div>
---

## Bounded Contexts et Context Mapping

### Exemple d'Architecture

```mermaid
graph LR
    A["🛒 Commandes"] -->|🔄| B["📦 Livraisons"]
    A -->|📝| C["💰 Paiements"]
    B -->|📦| D["📍 Logistique"]

    style A fill:#e8f4ff
    style B fill:#fff9e8
    style C fill:#ffe8f4
    style D fill:#e8ffe8
```

### Types de Relations

| Relation | Description | Exemple |
|---|---|---|
| **Partnership** | Collaboration étroite | Commandes ↔ Livraisons |
| **Customer-Supplier** | Client-fournisseur | Commandes → Paiements |
| **Conformist** | Adaptation | Livraisons → Logistique |
| **Anti-Corruption Layer** | Isolation | Legacy → Nouveau |

---

## Event Storming

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>

### Processus Collaboratif

```mermaid
graph TD
    A["🤝 Atelier"] --> B["📝 Événements"]
    B --> C["🔷 Commandes"]
    C --> D["📦 Aggregates"]
    D --> E["🎯 Bounded Contexts"]

    style A fill:#ffd700
    style B fill:#e8f4ff
    style C fill:#fff9e8
    style D fill:#ffe8f4
    style E fill:#e8ffe8
```
</div>
<div>

### Étapes Clés

1. **Événements métiers**: "CommandePayée", "LivraisonPlanifiée"
2. **Commandes**: Actions déclenchantes
3. **Aggregates**: Groupes cohérents
4. **Bounded Contexts**: Frontières logiques

</div>
</div>

---

## Exemple (source : https://draft.io/fr/example/eventstorming)

![Exemple d'Event Storming](https://draft.io/assets/site/examples/light/fr/2400/example-eventstorming-362441cc6869cb7a6a6b5ccf05096c93.webp)

---

## Récapitulatif DDD

### Avantages

- **Alignement métier**: Langage commun
- **Modularité**: Contextes indépendants
- **Maintenabilité**: Modèle clair
- **Évolutivité**: Adaptation facile

### Anti-Patterns à Éviter

- **Big Ball of Mud**: Tout dans un contexte
- **Anemic Domain Model**: Logique dans les services
- **Over-Engineering**: Complexité inutile