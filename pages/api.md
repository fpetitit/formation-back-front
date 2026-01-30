---
layout: new-section
sectionImage: 'https://centralesupelec.venture.fr/wp-content/uploads/2023/06/cropped-Logo-CentraleSupelecVenture-VBk.png'
---

Les API : REST vs GraphQL

---

## REST vs GraphQL

### Comparaison des approches

| Aspect | REST | GraphQL |
| --- | --- | --- |
| Requête | Fixed endpoints (/users/1) | Flexible query (demander exactement ce qu'on veut) |
| Over-fetching | Oui (données superflues) | Non (données exactes) |
| Under-fetching | Oui (appels multiples) | Non (1 requête) |
| Caching | Facile (HTTP standard) | Plus difficile |
| Versioning | Nécessaire (/v1/, /v2/) | Pas nécessaire |
| Courbe d'apprentissage | Facile | Modérée |

---

## REST: Principes fondamentaux

### Principes clés:

REST: Representational State Transfer

- Client-Server: Séparation des préoccupations
- Stateless: Chaque requête contient toutes les infos
- Cacheable: Réponses peuvent être mises en cache
- Uniform Interface: Ressources identifiables par URI
- Méthodes HTTP standards: GET, POST, PUT, DELETE, PATCH

#### Exemple d'endpoints REST:

```plaintext
GET    /api/v1/contracts              # Récupérer tous les contrats
POST   /api/v1/contracts              # Créer un nouveau contrat
GET    /api/v1/contracts/123          # Récupérer un contrat spécifique
PUT    /api/v1/contracts/123          # Mettre à jour complètement
PATCH  /api/v1/contracts/123          # Mise à jour partielle
DELETE /api/v1/contracts/123          # Supprimer

GET    /api/v1/contracts/123/claims   # Sous-ressources
```

---

## REST: Bonnes pratiques

### Best practices pour une API REST robuste:

#### 🔐 Sécurité

- OAuth2: Authentification
- JWT: Token sans état
- HTTPS: Chiffrement
- Rate limiting: Protection DOS
- CORS: Contrôle d'accès

#### 📝 Versioning

- URL versioning: /v1/, /v2/
- Header versioning: X-API-Version
- Semantic versioning: 1.2.3
- Backward compatibility
- Deprecation warning

#### 📚 Documentation

- Swagger/OpenAPI
- Postman
- Réducers
- Exemples de requêtes
- Codes d'erreur

#### ⚠️ Erreurs

- Codes HTTP corrects
- Réponses d'erreur cohérentes
- Messages clairs
- Logging et monitoring
- Ratelimit headers

---

## Codes HTTP et gestion d'erreurs

#### Réponse d'erreur standardisée:

```plaintext
{
  "error": {
    "code": "INVALID_CONTRACT",
    "message": "Le contrat ne peut pas être créé",
    "details": {
      "field": "customer_id",
      "reason": "Customer not found"
    },
    "timestamp": "2026-01-17T10:30:00Z",
    "requestId": "req-12345"
  }
}
```

| Code | Signification | Exemple |
| --- | --- | --- |
| 200 | OK - Succès | Requête GET réussie |
| 201 | Created - Ressource créée | POST réussi |
| 400 | Bad Request - Erreur client | JSON invalide |
| 401 | Unauthorized - Auth requise | Token expiré |
| 403 | Forbidden - Pas d'accès | Permissions insuffisantes |
| 404 | Not Found - Ressource absente | Contrat inexistant |
| 500 | Server Error - Erreur serveur | Exception non gérée |
| 503 | Service Unavailable | Maintenance, surcharge |

---

## GraphQL: Introduction

### Concept clé: Demander exactement ce qu'on veut

#### ❌ REST (over-fetching)

```plaintext
GET /api/v1/contracts/123

{
  "id": "123",
  "customer": { ... },
  "premium": 1200,
  "type": "AUTO",
  "status": "ACTIVE",
  "createdAt": "...",
  "updatedAt": "...",
  // Plein de données non nécessaires
}

Données non utilisées = 
bande passante gaspillée
```

#### ✅ GraphQL (seulement ce qu'il faut)

GraphQL: Query language pour APIs

```plaintext
query {
  contract(id: "123") {
    id
    premium
    type
  }
}

Réponse:
{
  "contract": {
    "id": "123",
    "premium": 1200,
    "type": "AUTO"
  }
}

Que ce qui est demandé
```

---

## Schéma GraphQL

#### Exemple de schéma pour assurance:

Structure typée des données et opérations disponibles

```plaintext
type Contract {
  id: ID!                    # ! = obligatoire
  customer: Customer!
  premium: Float!
  type: ContractType!
  status: Status!
  claims: [Claim!]!          # Liste obligatoire
  createdAt: DateTime!
}

type Customer {
  id: ID!
  name: String!
  email: String!
  age: Int!
  contracts: [Contract!]!
}

enum ContractType {
  AUTO
  HOME
  HEALTH
}

enum Status {
  ACTIVE
  EXPIRED
  SUSPENDED
}

type Query {
  contract(id: ID!): Contract
  contracts(limit: Int = 10): [Contract!]!
  customer(id: ID!): Customer
}

type Mutation {
  createContract(input: CreateContractInput!): Contract!
  updateContract(id: ID!, input: UpdateContractInput!): Contract!
  deleteContract(id: ID!): Boolean!
}
```

---

## GraphQL Queries (Lecture)

### Query simple:

```plaintext
query GetContract {
  contract(id: "123") {
    id
    premium
    type
    customer {
      name
      email
    }
  }
}
```

### Query avec filtrage et pagination:

```plaintext
query GetContracts {
  contracts(limit: 10, offset: 0) {
    id
    premium
    type
    status
    customer {
      id
      name
    }
  }
}
```

### Query avec relations imbriquées:

```plaintext
query GetCustomerWithContracts {
  customer(id: "cust-1") {
    id
    name
    contracts {
      id
      premium
      type
      claims {
        id
        status
        amount
      }
    }
  }
}
```

---

## GraphQL Mutations (Écriture)

#### Mutation: Créer un contrat

Opérations de création, mise à jour, suppression

```plaintext
mutation CreateNewContract {
  createContract(input: {
    customerId: "cust-1"
    type: AUTO
    coverage: [COLLISION, THEFT]
    deductible: 500
  }) {
    id
    premium
    status
    customer {
      name
    }
  }
}

Réponse:
{
  "createContract": {
    "id": "contract-789",
    "premium": 1200.50,
    "status": "ACTIVE",
    "customer": {
      "name": "John Doe"
    }
  }
}
```

---

## GraphQL: Avantages et limitations

#### ✅ Avantages

#### ❌ Limitations

- Pas de over-fetching
- Pas de under-fetching
- Requête unique
- Pas de versioning
- Typage fort
- Documentation auto
- Introspection

- Caching difficile (POST)
- Courbe apprentissage
- Complexité du serveur
- N+1 queries problem
- File uploads complexe
- Real-time (WebSocket)
- Monitoring plus difficile

---

## Quand utiliser REST vs GraphQL?

| Scénario | REST | GraphQL | Recommandation |
| --- | --- | --- | --- |
| Ressources simples | ✅ Idéal | ⚠️ Overkill | REST |
| Relations complexes | ❌ Appels multiples | ✅ Requête unique | GraphQL |
| Clients variés | ❌ Over-fetching | ✅ Données précises | GraphQL |
| Mobile (bande passante) | ❌ Données superflues | ✅ Minimal | GraphQL |
| Caching HTTP | ✅ Facile | ❌ Complexe | REST |
| Adoption rapide | ✅ Facile à apprendre | ❌ Courbe apprentissage | REST |
| Real-time (WebSocket) | ❌ Non natif | ✅ Subscriptions | GraphQL |
| File uploads | ✅ Natif | ⚠️ Complexe | REST |

---

## Sécurité dans les APIs

#### 🔐 OAuth2

Protocole d’autorisation qui permet à une application tierce d’accéder à des ressources protégées (API, données) au nom d’un utilisateur, sans lui transmettre son mot de passe

#### 🔑 JWT (JSON Web Tokens)

Standard ouvert pour transmettre des informations sécurisées sous forme d'objet JSON signé numériquement.

#### 🔐 OpenID Connect

Protocole d'authentification basé sur OAuth 2.0 qui vérifie l'identité des utilisateurs via un ID Token (JWT).
Il ajoute à OAuth une couche d'identité standardisée (openid scope) pour SSO et informations utilisateur sécurisées.



---

## Documentation API: Swagger/OpenAPI

#### Exemple de specification OpenAPI (YAML):

Documenter et tester les APIs interactivement

```plaintext
openapi: 3.0.0
info:
  title: Insurance API
  version: 1.0.0
paths:
  /contracts:
    get:
      summary: List all contracts
      parameters:
        - name: limit
          in: query
          type: integer
          default: 10
      responses:
        '200':
          description: List of contracts
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Contract'
        '401':
          description: Unauthorized
    post:
      summary: Create contract
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateContractRequest'
      responses:
        '201':
          description: Contract created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Contract'
components:
  schemas:
    Contract:
      type: object
      properties:
        id:
          type: string
        premium:
          type: number
        type:
          type: string
```

---

## Versioning d'API

#### 🔢 URL Versioning

Maintenir la compatibilité avec les clients existants

- Semantic Versioning: MAJOR.MINOR.PATCH (1.2.3)
- Backward compatibility: Supporter les anciennes versions (minimum 2 ans)
- Deprecation warnings: Notifier les clients
- Changelog: Documenter les changements

```plaintext
GET /api/v1/contracts
GET /api/v2/contracts

Avantages:
✅ Clair et explicite
✅ Caching facile
✅ Fournisseurs multiples

Inconvénients:
❌ URLs dupliquées
❌ Maintenance double
```

#### 📋 Header Versioning

```plaintext
GET /api/contracts
X-API-Version: 2

Avantages:
✅ URL unique
✅ Moins de duplication

Inconvénients:
❌ Moins visible
❌ Caching plus difficile
```

---

## Récapitulatif: API et GraphQL

#### 🌐 REST API

- Standard HTTP (GET, POST, PUT, DELETE)
- Endpoints fixes par ressource
- Facile à cacher
- Versioning standard
- Idéal pour ressources simples
- Courbe apprentissage faible

#### 📊 GraphQL

- Query language typé
- Requêtes flexibles
- Pas over/under-fetching
- Pas de versioning
- Idéal pour relations complexes
- Courbe apprentissage modérée

### Points clés:

- ✅ Sécurité: OAuth2 + JWT
- ✅ Documentation: Swagger/OpenAPI
- ✅ Versioning: URL ou Header
- ✅ Codes HTTP corrects
- ✅ Gestion d'erreurs cohérente