# 🚀 Caching Avancé

---

## Patterns de Cache

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">

<div>

### Cache-Aside (Lazy Loading)

```mermaid
sequenceDiagram
    participant Client
    participant Cache
    participant Database

    Client->>Cache: Demande donnée
    alt Cache hit
        Cache->>Client: Retourne donnée
    else Cache miss
        Cache->>Database: Récupère donnée
        Database->>Cache: Stocke donnée
        Cache->>Client: Retourne donnée
    end
```
</div>
<div>

### Write-Through

```mermaid
sequenceDiagram
    participant Client
    participant Cache
    participant Database

    Client->>Cache: Écrit donnée
    Cache->>Database: Écrit donnée
    Database->>Cache: Confirmation
    Cache->>Client: Confirmation
```
</div>
</div>

---

## Stratégies d'Invalidation

### 1. Time-based (TTL)

```mermaid
graph LR
    A["🕒 Donnée mise en cache"] --> B["⏳ TTL expire"]
    B --> C["🗑️ Invalidation automatique"]

    style A fill:#e8f4ff
    style B fill:#fff9e8
    style C fill:#ffe8f4
```

### 2. Event-based

```mermaid
graph LR
    A["📝 Mise à jour BD"] --> B["🔔 Événement"]
    B --> C["🗑️ Invalidation cache"]

    style A fill:#e8f4ff
    style B fill:#ffd700
    style C fill:#ffe8f4
```

---

## Comparaison Redis vs Memcached

| Critère | Redis | Memcached |
|---|---|---|
| **Persistance** | ✅ Oui | ❌ Non |
| **Structures** | ✅ Riches | ❌ Clé-valeur |
| **Réplication** | ✅ Master-Slave | ❌ Basique |
| **Performance** | ⚠️ Très élevée | ✅ Extrême |
| **Utilisation** | Cache + BD | Cache pur |

### Cas d'usage

- **Redis**: Sessions, leaderboards, pub/sub
- **Memcached**: Cache simple, performances pures