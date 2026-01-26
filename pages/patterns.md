---

# 🏗️ Patterns d'Architecture

*Solutions éprouvées pour structurer vos applications*

---

## Pourquoi utiliser des patterns ?

### Les patterns résolvents des problèmes récurrents

> "The purpose of design patterns is to give a name and a context to design problems and their solutions." — **Gang of Four**, Design Patterns

![Design Patterns](https://covers.openlibrary.org/b/isbn/0201633612-L.jpg)

- Réutilisabilité: Solutions éprouvées et documentées
- Standardisation: Équipes alignées sur une même approche
- Collaboration: Facilite la communication entre développeurs
- Réduction des risques: Évite les pièges courants
- Maintenabilité: Code plus prévisible et compréhensible

---

## Pattern Dependency Injection (DI)
Injecter les dépendances plutôt que les créer soi-même.

### Sans Dependency Injection (couplage fort):


```plaintext
public class ContractService {
    private DatabaseService db = new DatabaseService(); // Couplage fort
    
    public void createContract(Contract c) {
        db.save(c);
    }
}
```

### Avec Dependency Injection (découplage):


```plaintext
public class ContractService {
    private DatabaseService db; // Interface
    
    @Inject // Spring
    public ContractService(DatabaseService db) {
        this.db = db;
    }
}
```

---

## Pattern MVC (Model-View-Controller)

### Séparation des responsabilités:

- Model: Données et logique métier
- View: Présentation et interface utilisateur
- Controller: Coordination et gestion des événements

```mermaid
graph LR
                            User["👤 Utilisateur"] -->|Interaction| View["🎨 View<br/>(Présentation)"]
                            View -->|Événement| Controller["⚙️ Controller<br/>(Logique)"]
                            Controller -->|Update| Model["📊 Model<br/>(Données)"]
                            Model -->|Notify| View
                            
                            style User fill:#e8f4ff
                            style View fill:#fff9e8
                            style Controller fill:#ffe8f4
                            style Model fill:#f4e8ff
```

---

## Pattern MVVM (Model-View-ViewModel)

### Caractéristiques:

- Binding bidirectionnel: Sync automatique View ↔ ViewModel
- Testabilité: ViewModel indépendant de la Vue
- Réactivité: Mises à jour temps réel

```mermaid
graph LR
                            View["🎨 View<br/>(UI)"]
                            ViewModel["🔗 ViewModel<br/>(Binding)"]
                            Model["📊 Model<br/>(Données)"]
                            
                            View -->|Two-way Binding| ViewModel
                            ViewModel -->|Data Binding| View
                            ViewModel -->|Update| Model
                            Model -->|Notify| ViewModel
                            
                            style View fill:#fff9e8
                            style ViewModel fill:#ffe8f4
                            style Model fill:#f4e8ff
```

---

## Pattern CQRS (Command Query Responsibility Segregation)

### Concept clé

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>
Séparer les modèles de lecture et écriture pour optimiser chacun indépendamment.

### Avantages

- ✅ **Optimisation indépendante**: Chaque modèle optimisé pour son usage
- ✅ **Scalabilité**: Lectures et écritures peuvent être déployées séparément
- ✅ **Performance**: Read DB peut être dénormalisée (cache, index spécifiques)
- ✅ **Clarté**: Séparation claire des responsabilités

</div>
<div>
```mermaid
graph LR
    subgraph Commands["📝 CÔTÉ ÉCRITURE (Commands)"]
        UI1["🧑 Utilisateur<br/>Modifie"]
        Handler1["⚡ Command<br/>Handler"]
        Domain["🎯 Domain<br/>Model"]
        WriteDB["💾 Write DB<br/>Optimisée"]
        EventBus["📢 Event<br/>Bus"]
    end

    subgraph Queries["🔍 CÔTÉ LECTURE (Queries)"]
        UI2["🧑 Utilisateur<br/>Consulte"]
        Handler2["⚡ Query<br/>Handler"]
        ReadDB["📖 Read DB<br/>Dénormalisée"]
    end

    UI1 -->|Créer<br/>Modifier| Handler1
    Handler1 -->|Logique métier| Domain
    Domain -->|Persist| WriteDB
    Domain -->|Publie| EventBus

    UI2 -->|Chercher<br/>Afficher| Handler2
    Handler2 -->|Accès rapide| ReadDB

    EventBus -->|Synchronise| ReadDB

    style Commands fill:#ffe8f4
    style Queries fill:#fff9e8
    style WriteDB fill:#ffe8e8
    style ReadDB fill:#e8ffe8
    style EventBus fill:#f4e8ff
```
</div>
</div>
---

## Architecture Event-Sourcing

### Principes fondamentaux

```mermaid
graph LR
    A["📝 Événements"] --> B["🗄️ Event Store"]
    B --> C["🔄 Replay"]
    C --> D["📊 État actuel"]
    B --> E["📈 Projections"]
    E --> F["🖥️ Vues optimisées"]

    style A fill:#e8f4ff
    style B fill:#fff9e8
    style C fill:#ffe8f4
    style D fill:#e8ffe8
    style E fill:#f4e8ff
    style F fill:#ffebe8
```

### Concepts clés

- **Événements immutables**: Tous les changements sont stockés comme événements
- **Reconstruction d'état**: L'état actuel est reconstruit en replayant les événements
- **Projections**: Vues optimisées pour différents cas d'usage
- **Audit trail**: Historique complet de toutes les modifications

---

### Cas d'usage

- **Finance**: Traçabilité complète des transactions
- **Assurance**: Historique des contrats et sinistres
- **Santé**: Dossiers patients avec historique complet

### Outils populaires

- **EventStoreDB**: Base de données dédiée
- **Kafka**: Pour le streaming d'événements
- **Axoni**: Plateforme complète

---

## Comparaison Event-Sourcing vs CRUD

| Aspect | Event-Sourcing | CRUD Traditionnel |
|---|---|---|
| **Historique** | ✅ Complet | ❌ Partiel |
| **Audit** | ✅ Natif | ❌ Requiert logs |  |
| **Performance lecture** | ❌ Replay nécessaire | ✅ Direct |
| **Complexité** | ⚠️ Élevée | ✅ Simple |
| **Évolutivité** | ✅ Excellente | ⚠️ Limitée |

---

## Pattern Event-Driven Architecture

### Cas d'usage assurance:

Services réactifs aux événements métiers asynchrones.

- Événement: "ContractCreated" - Un nouveau contrat est créé
- Consommateurs: Service email (notification), Service CRM (update), Service audit (logging)
- Avantage: Découplage complet entre services

```mermaid
graph LR
                            A["Producteur<br/>(Service)"] -->|Publie| Broker["🔔 Event Broker<br/>(Kafka, RabbitMQ)"]
                            Broker -->|Consomme| B["Consommateur 1<br/>(Service)"]
                            Broker -->|Consomme| C["Consommateur 2<br/>(Service)"]
                            Broker -->|Consomme| D["Consommateur N<br/>(Service)"]
                            
                            style A fill:#e8f4ff
                            style Broker fill:#ffe8f4
                            style B fill:#fff9e8
                            style C fill:#e8ffe8
                            style D fill:#f4e8ff
```

---

## Pattern Hexagonal (Ports & Adapters)

### Bénéfices:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 0px;">
<div>
Isoler le cœur métier des détails techniques.

- Cœur métier indépendant des frameworks
- Adaptation facile aux changements technologiques
- Tests unitaires sans dépendances externes

</div>
<div>

```mermaid
graph TB
                            UI["UI / API"]
                            DB["Base de données"]
                            MAIL["Service email"]
                            API3["API tierce"]
                            
                            UI -->|Port| Core["🔷 Cœur Métier<br/>(Logique pure)"]
                            Core -->|Port| DB
                            Core -->|Port| MAIL
                            Core -->|Port| API3
                            
                            UAda["Web Adapter"]
                            DBAda["PostgreSQL Adapter"]
                            MAILAda["SMTP Adapter"]
                            APIAda["HTTP Adapter"]
                            
                            UAda -.->|Implémente| UI
                            DBAda -.->|Implémente| DB
                            MAILAda -.->|Implémente| MAIL
                            APIAda -.->|Implémente| API3
                            
                            style Core fill:#fff9e8,stroke:#ffc107,stroke-width:3px
                            style UI fill:#e8f4ff
                            style DB fill:#f4e8ff
                            style MAIL fill:#e8ffe8
                            style API3 fill:#ffe8f4
```
</div>
</div>
---

## Pattern Repository

### Avantages:

Abstraction de la couche d'accès aux données.

- Logique métier indépendante du mécanisme de persistance
- Facile de basculer de PostgreSQL à MongoDB
- Tests unitaires avec implémentation mock

```mermaid
graph LR
                            Service["Service métier<br/>(ContractService)"]
                            Repo["Repository Interface<br/>(IContractRepository)"]
                            Impl1["Implémentation DB<br/>(PostgresContractRepository)"]
                            Impl2["Implémentation Cache<br/>(CachedContractRepository)"]
                            Impl3["Implémentation Mock<br/>(MockContractRepository)"]
                            
                            Service -->|Utilise| Repo
                            Repo -->|Implémenté par| Impl1
                            Repo -->|Implémenté par| Impl2
                            Repo -->|Implémenté par| Impl3
                            
                            style Service fill:#e8f4ff
                            style Repo fill:#fff9e8
                            style Impl1 fill:#f4e8ff
                            style Impl2 fill:#e8ffe8
                            style Impl3 fill:#ffe8f4
```

---

## Récapitulatif: Quand utiliser quel pattern ?

| Pattern | Problème | Quand l'utiliser |
| --- | --- | --- |
| MVC | Séparation UI/logique | Web traditionnel, applications simples |
| MVVM | Binding bidirectionnel | Interfaces réactives, desktop/mobile |
| CQRS | Scalabilité lecture/écriture | Hauts volumes, complex queries |
| Event-Driven | Découplage asynchrone | Microservices, systèmes réactifs |
| Hexagonal | Isolation cœur métier | Logique métier complexe, DDD |
| DI | Gestion dépendances | Tous les projets modernes |
